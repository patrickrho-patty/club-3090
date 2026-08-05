#!/usr/bin/env bash
# Launch the Qwen3.6-35B-A3B SFT (W4A16 AutoRound) model on vLLM across TWO GPUs
# (TP=2) using the club-3090 dual-card recipe — full 262K context + cudagraph
# (eager off) + fp8_e4m3 KV + chunked prefill, for max decode TPS.
#
# This is the DUAL-CARD counterpart to launch_qwen36_sft_w4a16_vllm.sh (which is
# the single-card fallback). Same container name (ssq-llm-sft), same port (8033),
# same bind (10.200.82.233) — drop-in replacement, consumers (apps/api + k8s)
# unchanged. Served-model-name stays lex-llm-sft.
#
# Why W4A16 AutoRound: we quantized our own SFT into this format ON PURPOSE so it
# matches the club-3090 speed stack (autoround-int4 experts + BF16 routers loads
# on vLLM's fp8_e4m3 KV / FlashInfer / cudagraph path). This is what lets a
# fine-tuned model ride club-3090's tuned dual-3090 throughput.
#
# Model lineage (all private, patrick-patty HF org):
#   CPT   qwen36-35b-a3b-cpt-kr-legal-20pct-merged
#   SFT   qwen36-35b-a3b-sft-curated-v2-52k-merged   (LoRA r16, 52k curated)
#   QUANT qwen36-35b-a3b-sft-w4a16-autoround          <- served here
# Repo: https://huggingface.co/patrick-patty/qwen36-35b-a3b-sft-w4a16-autoround
#
# Recipe adapted from models/qwen3.6-35b-a3b/vllm/compose/dual/autoround-int4/fp8.yml
# Deviations from that base compose (behavior-preserving for the SFT):
#   - weights      = our SFT (not the base autoround)
#   - served-name / port / bind kept (consumer compatibility)
#   - chat-template = SFT's own (we do NOT force the froggeric template)
#   - tool/reasoning parsers OMITTED (qwen3_coder / qwen3 reasoning are base-model
#     QoS flags; not trained into this SFT and may break its format)
# Performance recipe applied unchanged: TP=2, 262K, fp8_e4m3 KV, eager OFF,
# chunked prefill, prefix caching, --disable-custom-all-reduce (PCIe, no NVLink).
# Qwen3.6 thinking-mode defaults baked in via --override-generation-config
# (temp 1.0 / top_p 0.95 / top_k 20 / presence_penalty 1.5 — official model-card
# values for enable_thinking=true general tasks) + --default-chat-template-kwargs
# enable_thinking=true so thinking is on by default. Clients can still override
# per-request; pass extra_body.chat_template_kwargs.enable_thinking=false to mute.
# --reasoning-parser qwen3: splits <think>...</think> into reasoning_content
# (template opens <think>, model closes </think>) so content is the clean answer
# and thinking is a separate parseable field — LiteLLM forwards reasoning_content.
#
# GPU layout: 0 + 1 (TP=2). GPU2 is reserved for the search-stack-quant
# (reranker/embedding/router/mineru) and is NEVER touched by this script.
#
# Usage: launch_qwen36_sft_dual.sh [start|stop|status|restart|logs]
# Env overrides:
#   MODEL_PATH   (default /data/projects/club-3090/models-cache/qwen36-35b-a3b-sft-w4a16-autoround)
#   GPUS         (default 0,1)         — must be exactly 2 for TP=2
#   PORT         (default 8033)
#   BIND_HOST    (default 10.200.82.233)
#   MAX_MODEL_LEN (default 262144)
#   GPU_MEM_UTIL (default 0.92)
#   MAX_NUM_SEQS (default 1; raise to 8 + LONG_PREFILL_TOKEN_THRESHOLD=2560 for agentic)
#   VLLM_IMAGE   (default vllm/vllm-openai:v0.25.1)

set -euo pipefail

CONTAINER_NAME="${CONTAINER_NAME:-ssq-llm-sft}"
PORT="${PORT:-8033}"
BIND_HOST="${BIND_HOST:-10.200.82.233}"
GPUS="${GPUS:-0,1}"
MODEL_PATH="${MODEL_PATH:-/data/projects/club-3090/models-cache/qwen36-35b-a3b-sft-w4a16-autoround}"
MAX_MODEL_LEN="${MAX_MODEL_LEN:-262144}"
GPU_MEM_UTIL="${GPU_MEM_UTIL:-0.92}"
MAX_NUM_SEQS="${MAX_NUM_SEQS:-1}"
MAX_NUM_BATCHED_TOKENS="${MAX_NUM_BATCHED_TOKENS:-8192}"
LONG_PREFILL_TOKEN_THRESHOLD="${LONG_PREFILL_TOKEN_THRESHOLD:-0}"
IMAGE="${VLLM_IMAGE:-vllm/vllm-openai:v0.25.1}"

cmd="${1:-start}"

stop() {
    echo "Stopping $CONTAINER_NAME ..."
    docker rm -f "$CONTAINER_NAME" 2>/dev/null && echo "Stopped." || echo "Not running."
}

start() {
    if [ ! -d "$MODEL_PATH" ]; then
        echo "ERROR: MODEL_PATH not found: $MODEL_PATH"
        echo "Pull it first: huggingface-cli download patrick-patty/qwen36-35b-a3b-sft-w4a16-autoround --local-dir $MODEL_PATH"
        exit 1
    fi
    echo "Starting $CONTAINER_NAME on GPUs $GPUS (TP=2), port $BIND_HOST:$PORT ..."
    docker rm -f "$CONTAINER_NAME" 2>/dev/null || true
    docker run -d \
      --name "$CONTAINER_NAME" \
      --restart unless-stopped \
      --gpus "\"device=$GPUS\"" \
      -e NVIDIA_VISIBLE_DEVICES="$GPUS" \
      -e VLLM_WORKER_MULTIPROC_METHOD=spawn \
      -e NCCL_P2P_DISABLE=1 \
      -e NCCL_CUMEM_ENABLE=0 \
      -e NCCL_IB_DISABLE=1 \
      -e VLLM_NO_USAGE_STATS=1 \
      -e PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
      -e OMP_NUM_THREADS=1 \
      --ipc=host \
      --shm-size=16g \
      -v "$MODEL_PATH:/model:ro" \
      -p "$BIND_HOST:$PORT:8000" \
      "$IMAGE" \
      --host 0.0.0.0 --port 8000 \
      --model /model \
      --served-model-name lex-llm-sft \
      --quantization auto_round \
      --dtype float16 \
      --tensor-parallel-size 2 \
      --pipeline-parallel-size 1 \
      --max-model-len "$MAX_MODEL_LEN" \
      --gpu-memory-utilization "$GPU_MEM_UTIL" \
      --max-num-seqs "$MAX_NUM_SEQS" \
      --max-num-batched-tokens "$MAX_NUM_BATCHED_TOKENS" \
      --limit-mm-per-prompt '{"image":2,"audio":0}' \
      --kv-cache-dtype fp8_e4m3 \
      --disable-custom-all-reduce \
      --trust-remote-code \
      --enable-prefix-caching \
      --enable-chunked-prefill \
      --override-generation-config '{"temperature":1.0,"top_p":0.95,"top_k":20,"min_p":0.0,"presence_penalty":1.5,"repetition_penalty":1.0}' \
      --default-chat-template-kwargs '{"enable_thinking": true}' \
      --reasoning-parser qwen3 \
      $([ "$LONG_PREFILL_TOKEN_THRESHOLD" != "0" ] && echo --long-prefill-token-threshold "$LONG_PREFILL_TOKEN_THRESHOLD") \
      && echo "Container started. Waiting for health (TP=2 + cudagraph compile takes ~3-4 min on first boot)..."

    for i in $(seq 1 60); do
        if curl -sf "http://$BIND_HOST:$PORT/health" >/dev/null 2>&1; then
            echo "Healthy after $((i*5))s!"
            return 0
        fi
        sleep 5
    done
    echo "WARNING: not healthy after 300s. Recent logs:"
    docker logs --tail 30 "$CONTAINER_NAME"
    return 1
}

status() {
    docker ps --filter "name=$CONTAINER_NAME" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
    if curl -sf "http://$BIND_HOST:$PORT/v1/models" >/dev/null 2>&1; then
        echo "API: responding"
        curl -s "http://$BIND_HOST:$PORT/v1/models" | python3 -c "import json,sys;d=json.load(sys.stdin);print('  model:',d['data'][0]['id'],'| max_model_len:',d['data'][0].get('max_model_len'))" 2>/dev/null || true
    else
        echo "API: not responding"
    fi
}

logs() { docker logs --tail 50 "$CONTAINER_NAME"; }

case "$cmd" in
    start)   start ;;
    stop)    stop ;;
    status)  status ;;
    restart) stop; start ;;
    logs)    logs ;;
    *) echo "Usage: $0 [start|stop|status|restart|logs]"; exit 1 ;;
esac
