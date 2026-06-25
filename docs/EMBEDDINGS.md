# Embedding models on RTX 3090

Transformer-based embedding models (Qwen3-Embedding-0.6B/4B/8B, GTE, BGE, etc.)
share the same architecture as the generative LLMs this repo serves.
Most of the techniques we use to maximize generative TPS **transfer directly**
to embedding throughput — same weights, same attention, same CUDA kernels,
just no autoregressive decoding loop.

This doc maps each club-3090 technique to its embedding applicability,
so you can build an embedding compose that reuses the stack we already have.

---

## What's different about embedding workloads

| Property | Generative (LLM) | Embedding |
|---|---|---|
| Forward pass | Prefill + decode loop | Prefill only (encode) |
| KV cache growth | Grows per token generated | Single-pass, no accumulation |
| Output | Token stream | Single pooled vector |
| Batch pattern | Few long sequences | Many short sequences |
| Bottleneck | Decode memory bandwidth | Prefill compute (matmuls) |
| Typical input length | 1K–262K tokens | 512–8192 tokens |
| `max_model_len` need | As high as VRAM allows | Low — frees VRAM for batching |

**Key insight:** embedding is *prefill-only*. Every technique that speeds up
prefill (weight quant, TP, Flash Attention, CUDA graphs, torch.compile) helps
directly. Decode-specific techniques (speculative decoding, KV offload,
continuous KV growth management) don't apply.

---

## Techniques that transfer directly

### 1. Weight quantization

The single biggest win. Smaller weights = more VRAM for batches = higher throughput.

| Technique | How it helps | Repo reference |
|---|---|---|
| **AutoRound INT4** | ~4× VRAM reduction, Marlin GEMM kernels on Ampere | `models/*/vllm/compose/*/autoround-int4/` |
| **AWQ INT4** | Same class, different calibration | `models/gemma-4-26b-a4b/vllm/compose/dual/awq/` |
| **GPTQ INT4** | Classic PTQ, wide tool support | Supported in vLLM via `--quantization gptq` |
| **FP8 weights** | Storage-only on sm_86 (Marlin W8A16 dequant) | `scripts/lib/profiles/models/qwen3.6-27b.yml` |

For a 4B embedding model, INT4 quant brings weights from ~8 GB (BF16) down to ~2 GB,
leaving ~20 GB on a single 3090 for batch activations and KV.

**vLLM flag:** `--quantization auto_round` (or `awq` / `gptq` depending on the weights artifact).

### 2. Tensor Parallelism (TP=2)

Identical to generative TP — splits weight matrices across GPUs.

```yaml
# From any dual compose in this repo:
command: >-
  --tensor-parallel-size 2
  --disable-custom-all-reduce    # PCIe-only, no NVLink
environment:
  NCCL_CUMEM_ENABLE: "0"
  NCCL_P2P_DISABLE: "${NCCL_P2P_DISABLE:-0}"  # detect_nvlink.sh sets this
```

Reference: every `dual/` compose + `scripts/detect_nvlink.sh`.

### 3. CUDA kernels and compile caching

| Technique | What it does | Compose reference |
|---|---|---|
| **torch.compile cache** | JIT-compiles graphs; first boot ~60-90s, then reuses | Volume: `cache/torch_compile` |
| **Triton kernel cache** | Cached custom kernels across restarts | Volume: `cache/triton` |
| **Marlin INT4 GEMM** | Fast dequant+matmul for INT4 weights on Ampere | `vllm/patches/vllm-marlin-pad/` |
| **Flash Attention** | Fused attention — benefits encode passes identically | Default in vLLM; `--flash-attn on` in llama.cpp |
| **CUDA graphs** | Captures and replays GPU ops — embedding batches have uniform shapes, ideal for graph capture | Don't set `--enforce-eager` |

### 4. Memory management

```yaml
command: >-
  --gpu-memory-utilization 0.95        # higher than generative — no KV growth headroom needed
  --max-model-len 8192                 # embedding inputs are short — frees massive VRAM
  --max-num-seqs 64                    # crank up — embedding requests are short-lived
  --max-num-batched-tokens 16384       # more tokens per forward pass = higher throughput
environment:
  PYTORCH_CUDA_ALLOC_CONF: "expandable_segments:True,max_split_size_mb:512"
  OMP_NUM_THREADS: "1"                 # prevents thread oversubscription
```

**Contrast with generative:** generative composes use `max_num_seqs: 2`,
`max_model_len: 262144`, `gpu_memory_utilization: 0.92`. Embedding flips these:
short contexts, many concurrent requests, tighter VRAM budget for weights+activations.

### 5. Prefix caching

If you embed many documents with shared task instructions (e.g., the
`Instruct:` prefix in Qwen3-Embedding), prefix caching avoids re-computing
the shared prefix for every request.

```yaml
command: >-
  --enable-prefix-caching
```

### 6. Chunked prefill

Helps process long documents without blocking the entire GPU:

```yaml
command: >-
  --enable-chunked-prefill
```

### 7. Docker / deployment settings

Carry over as-is from any vLLM compose:

```yaml
shm_size: "16gb"
ipc: host
deploy:
  resources:
    reservations:
      devices:
        - driver: nvidia
          count: all        # or 1 for single-card
          capabilities: [gpu]
environment:
  VLLM_WORKER_MULTIPROC_METHOD: "spawn"
  VLLM_NO_USAGE_STATS: "1"
```

### 8. Power management

Embedding is prefill-heavy (compute-bound). The repo's power-cap sweep
(`scripts/power-cap-sweep.sh`) finds the efficiency knee. From the
3090 hardware profile (`scripts/lib/profiles/hardware/rtx-3090.yml`):

```yaml
power_cap_w_prefill: 250      # embedding sweet spot — compute-bound
power_cap_w_optimal: 290      # generative balance point
```

For sustained embedding throughput, 250–290W is the range to sweep.
Use `scripts/gpu-mode.sh` for quick on/off power caps.

---

## Techniques that need adaptation

### KV cache quantization (FP8 / INT8)

Embedding has no autoregressive KV growth, so this matters less.
But for batch-processing many sequences, quantized KV still saves VRAM
(the attention computation for each input still materializes KV).

- **FP8 e5m2 KV:** `--kv-cache-dtype fp8_e5m2` — storage-only on Ampere
- **INT8 per-token-head:** `--kv-cache-dtype int8_per_token_head` — works on Ampere

Worth testing: the VRAM savings may let you fit more concurrent sequences.

### Concurrency tuning

The repo's generative concurrency is calibrated for 1–4 streams.
Embedding wants maximum concurrency. Use the power-cap sweep methodology
(`scripts/power-cap-sweep.sh` decode-concurrent mode) but probe
embedding-specific saturation:

```bash
# Sweep concurrent embedding requests to find GPU saturation point
for conc in 8 16 32 64 128; do
  # measure embedding throughput at each concurrency level
done
```

### VRAM budget math

`tools/kv-calc.py` models KV growth for generative workloads. For embedding:
- No growing KV term — it's single-pass
- Budget = weights + (batch_size × seq_len × per_token_activation) + overhead
- More VRAM freed from KV = more batch capacity

---

## Techniques that do NOT transfer

| Technique | Why not |
|---|---|
| **Speculative decoding** (MTP, DFlash, EAGLE) | Generative-only — no token sampling in embedding |
| **Genesis patches** | Qwen3-Next-specific, retired upstream |
| **TurboQuant / KVarN KV** | Engine-specific, Genesis-dependent |
| **LMCache KV offload** | No cross-turn KV accumulation |
| **FlashInfer sampler** | No token sampling |
| **Chat templates / tool parsers** | Not relevant to embedding |
| **Cliff 2b mitigations** | No multi-turn KV accumulation |

---

## Skeleton compose for Qwen3-Embedding-4B

This is a starting point — adapt after benchmarking.

```yaml
# ===========================================================================
# Profile (at-a-glance):
#   Model:     Qwen3-Embedding-4B (BF16 — or INT4 if quantized weights available)
#   Topology:  Single 3090 (TP=1)
#   Drafter:   none (encode-only)
#   KV:        fp8_e5m2
#   Vision:    no
#   Max ctx:   8192
#   Genesis:   N/A — not a Qwen3-Next model
#   Status:    🧪 Experimental
#   Best for:  High-throughput document embedding
# ---------------------------------------------------------------------------
# Embedding-optimized compose for Qwen3-Embedding-4B on a single RTX 3090.
# Techniques transferred from the generative LLM composes in this repo.
# ===========================================================================

services:
  embedding:
    image: vllm/vllm-openai:v0.22.0
    ports:
      - "${PORT:-8030}:8000"
    volumes:
      - ${MODELS_CACHE:-../../models-cache}:/models
      # torch.compile + Triton caches (reuse across restarts)
      - ./cache/torch_compile:/root/.cache/vllm/torch_compile_cache
      - ./cache/triton:/root/.triton/cache
    environment:
      VLLM_WORKER_MULTIPROC_METHOD: "spawn"
      VLLM_NO_USAGE_STATS: "1"
      OMP_NUM_THREADS: "1"
      PYTORCH_CUDA_ALLOC_CONF: "expandable_segments:True,max_split_size_mb:512"
    command: >-
      --model /models/Qwen3-Embedding-4B
      --task embedding
      --dtype auto
      --max-model-len 8192
      --gpu-memory-utilization 0.95
      --max-num-seqs 64
      --max-num-batched-tokens 16384
      --kv-cache-dtype fp8_e5m2
      --enable-prefix-caching
      --enable-chunked-prefill
      --disable-log-requests
    shm_size: "16gb"
    ipc: host
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
```

### Dual-card variant

Add to the command:
```yaml
      --tensor-parallel-size 2
      --disable-custom-all-reduce
```
And set GPU count to `all` (or `2`).

### Smoke test

```bash
curl http://localhost:8030/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen3-Embedding-4B",
    "input": "The RTX 3090 has 24 GB of GDDR6X VRAM."
  }'
```

---

## What to benchmark

Once the compose boots, measure:

1. **Throughput** — embeddings/sec at increasing concurrency (8 → 16 → 32 → 64 → 128)
2. **Latency** — p50/p99 per-request at each concurrency level
3. **VRAM** — peak usage vs batch size (find the ceiling)
4. **Quality** — cosine similarity vs BF16 baseline (quantization fidelity check)
5. **Power** — sweep 250–350W to find the efficiency knee

The repo's `power-cap-sweep.sh` methodology applies directly — just swap
the generative prompt for an embedding request in the probe function.

---

## Next steps

- [ ] Source or quantize Qwen3-Embedding-4B weights (AutoRound INT4 if available on HF)
- [ ] Boot the skeleton compose, iterate on `max_num_seqs` / `max_num_batched_tokens`
- [ ] Run a concurrency sweep to find the GPU saturation point
- [ ] Measure quality delta (INT4 vs BF16 cosine similarity)
- [ ] If quality holds, add to the catalog via the `ADDING_MODELS.md` workflow
