# SSQ LLM-SFT — dual-card TP=2 deploy (our fine-tune on the club-3090 speed stack)

> Operational doc for serving **our own** Qwen3.6-35B-A3B legal SFT on GPU0+GPU1
> of `patricks-mint`, using club-3090's tuned dual-3090 recipe. GPU2 stays on the
> search-stack-quant (reranker/embedding/router/mineru) — never touched.

## What this is

We serve a model we trained ourselves, quantized into club-3090's format so it can
ride their optimized vLLM path (autoround-int4 → fp8_e4m3 KV → FlashInfer →
cudagraph). Result on 2× RTX 3090 (TP=2, no NVLink): **full 262K context**, ~2M-token
KV pool (7.6× concurrency), decode in the ~115–175 tok/s regime, vs the old
single-card eager serve that was capped at 8K context / 1 seq.

## Model — it IS our fine-tune

All repos private under the `patrick-patty` HF org. Full lineage:

| Stage | Repo | Notes |
|---|---|---|
| CPT | `patrick-patty/qwen36-35b-a3b-cpt-kr-legal-20pct-merged` | continued-pretrain, KR legal 20% |
| SFT | `patrick-patty/qwen36-35b-a3b-sft-curated-v2-52k-merged` | LoRA r16, 52k curated |
| **Quant (served)** | **`patrick-patty/qwen36-35b-a3b-sft-w4a16-autoround`** | W4A16 AutoRound, ~20 GB |

The `unsloth_fixed` / `unsloth_fixed_mtp` flags in `config.json` come from our own
quantization/export step — they are **not** a third-party-download marker.

### Why W4A16 AutoRound
We quantized on purpose to match club-3090's `dual/autoround-int4/fp8.yml` recipe —
INT4 experts + BF16 routers is exactly the format their tuned fp8_e4m3-KV /
FlashInfer / cudagraph path is validated against. This is the bridge that lets a
fine-tuned model inherit club-3090's measured dual-3090 throughput.

## How to run

```bash
# on patricks-mint, from the club-3090 checkout
bash scripts/launch_qwen36_sft_dual.sh start     # boot (first boot ~3-4 min: cudagraph compile)
bash scripts/launch_qwen36_sft_dual.sh status
bash scripts/launch_qwen36_sft_dual.sh logs
bash scripts/launch_qwen36_sft_dual.sh restart
bash scripts/launch_qwen36_sft_dual.sh stop
```

First-time / new machine — pull the weights (private, needs HF token):
```bash
huggingface-cli download patrick-patty/qwen36-35b-a3b-sft-w4a16-autoround \
  --local-dir /data/projects/club-3090/models-cache/qwen36-35b-a3b-sft-w4a16-autoround
```

## Serve identity (consumer-facing — do not change casually)

| Field | Value | Why |
|---|---|---|
| container name | `ssq-llm-sft` | monitoring / muscle memory |
| port | `10.200.82.233:8033 → 8000` | apps/api + k8s point here |
| served-model-name | `lex-llm-sft` | client `model` field |

## GPU layout

| GPU | Use | Touched by this script? |
|---|---|---|
| 0 | LLM-SFT (TP rank 0) | yes |
| 1 | LLM-SFT (TP rank 1) | yes |
| 2 | search-stack-quant (reranker/embedding/router/mineru) | **no** |

## Flags — the club-3090 recipe (what we apply)

Adapted from `models/qwen3.6-35b-a3b/vllm/compose/dual/autoround-int4/fp8.yml`:

- `--tensor-parallel-size 2` — weights + KV split across GPU0+1 (each card ~10 GB weights)
- `--max-model-len 262144` — model's full architectural max; DeltaNet-hybrid KV is cheap
- `--kv-cache-dtype fp8_e4m3` — 1 B/tok, routes to FlashInfer on sm_86
- **eager OFF** (no `--enforce-eager`) — cudagraph capture, the biggest decode lever
- `--enable-chunked-prefill --enable-prefix-caching`
- `--max-num-batched-tokens 8192`
- `--disable-custom-all-reduce` — **PCIe rig, no NVLink** (`nvidia-smi topo -m` = `PHB`)
- `--gpu-memory-utilization 0.92`
- env: `NCCL_P2P_DISABLE=1`, `NCCL_CUMEM_ENABLE=0`, `VLLM_WORKER_MULTIPROC_METHOD=spawn`, `--shm-size 16g`, `--ipc host`

## Flags — deliberately NOT set (deviations from base compose)

Behavior-preserving for our SFT — these base-model QoS flags are not trained in and
may break the SFT format:

- `--chat-template froggeric` → **omitted**, we use the SFT's own `chat_template.jinja`
- `--tool-call-parser qwen3_coder` / `--enable-auto-tool-choice` → omitted
- `--reasoning-parser qwen3` → omitted

If you want any of these, A/B against the SFT's eval set first — don't blind-flip.

## Agentic / multi-stream

Default `--max-num-seqs 1` (single-stream, safe). For multi-agent:
```bash
MAX_NUM_SEQS=8 LONG_PREFILL_TOKEN_THRESHOLD=2560 bash scripts/launch_qwen36_sft_dual.sh restart
```
(`LONG_PREFILL_TOKEN_THRESHOLD` must be ≥ 2560 — block size is 2096 at 262K. See
base compose header.)

## Tuning knobs (env)

`GPUS`, `PORT`, `BIND_HOST`, `MAX_MODEL_LEN`, `GPU_MEM_UTIL`, `MAX_NUM_SEQS`,
`MAX_NUM_BATCHED_TOKENS`, `VLLM_IMAGE`, `MODEL_PATH`. See script header.

## Single-card fallback

`scripts/launch_qwen36_sft_w4a16_vllm.sh` — the old single-GPU eager serve (8K
context). Use only if one GPU is down. ⚠️ That script has drift: header says
GPU 0,1 / 12K / bf16 but historically launched TP=1 float16. Reconcile if you
rely on it.

## Bench

For a decode TPS number comparable to club-3090's headline (174 tok/s decode for
the base model), use their harness with the served name:
```bash
MODEL=lex-llm-sft bash scripts/bench.sh
```
Wall-clock quick-probe (SFT, 20-tok prompt, includes prefill) ≈ 115–119 tok/s.
