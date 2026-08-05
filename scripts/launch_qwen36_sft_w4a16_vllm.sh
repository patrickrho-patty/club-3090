#!/usr/bin/env bash
# Launch the W4A16 quantized Qwen3.6-35B-A3B SFT model on vLLM.
# Deploys on GPUs 0+1 (48 GB total), port 8033.
#
# Usage: launch_qwen36_sft_w4a16_vllm.sh [start|stop|status]

set -euo pipefail

CONTAINER_NAME="ssq-llm-sft"
PORT=8033
MODEL_PATH="/data/projects/club-3090/models-cache/qwen36-35b-a3b-sft-w4a16-autoround"
GPU_DEVICES="0,1"
IMAGE="vllm/vllm-openai:latest"

cmd="${1:-start}"

stop() {
    echo "Stopping $CONTAINER_NAME..."
    docker rm -f "$CONTAINER_NAME" 2>/dev/null && echo "Stopped." || echo "Not running."
}

start() {
    echo "Starting $CONTAINER_NAME on GPUs $GPU_DEVICES, port $PORT..."
    docker run -d \
        --name "$CONTAINER_NAME" \
        --runtime nvidia \
        -e NVIDIA_VISIBLE_DEVICES="$GPU_DEVICES" \
        --ipc=host \
        --shm-size=4g \
        -v "$MODEL_PATH:/model" \
        -p "10.200.82.233:$PORT:8000" \
        "$IMAGE" \
        --model /model \
        --served-model-name lex-llm-sft \
        --dtype bfloat16 \
        --quantization auto-round \
        --max-model-len 12288 \
        --gpu-memory-utilization 0.88 \
        --max-num-seqs 16 \
        --enforce-eager \
        --trust-remote-code \
        --host 0.0.0.0 \
        --port 8000 \
        && echo "Container started. Waiting for health..."
    
    # Wait for health
    for i in $(seq 1 60); do
        if curl -sf "http://10.200.82.233:$PORT/health" >/dev/null 2>&1; then
            echo "Healthy after ${i}s!"
            return 0
        fi
        sleep 5
    done
    echo "WARNING: Container not healthy after 300s. Check logs:"
    docker logs --tail 20 "$CONTAINER_NAME"
    return 1
}

status() {
    docker ps --filter "name=$CONTAINER_NAME" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
    if curl -sf "http://10.200.82.233:$PORT/v1/models" >/dev/null 2>&1; then
        echo "API: responding"
        curl -s "http://10.200.82.233:$PORT/v1/models" | python3 -m json.tool 2>/dev/null || true
    else
        echo "API: not responding"
    fi
}

case "$cmd" in
    start) start ;;
    stop) stop ;;
    status) status ;;
    restart) stop; start ;;
    *) echo "Usage: $0 [start|stop|status|restart]"; exit 1 ;;
esac
