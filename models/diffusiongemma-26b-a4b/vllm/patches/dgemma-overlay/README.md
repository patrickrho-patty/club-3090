# DiffusionGemma sideload overlay (vllm#45163)

This directory is the **vendored payload** that turns a **stock, pullable** vLLM
nightly into a DiffusionGemma-capable engine at container start — *no baked
image*. `install.sh` (the compose entrypoint) cp's everything here over the
installed `vllm` package, drops stale bytecode, and fail-loud asserts the arch
registered.

Delivery is `install_script` (see `scripts/lib/profiles/patches.yml` →
`dgemma-vllm45163-sideload`). The compose `base.yml` mounts this dir to
`/etc/club3090/dgemma-overlay` and runs `install.sh` before `vllm` imports.

## Why the *full* branch delta, not the PR's 41-file set

DiffusionGemma's arch exists in **no** released/nightly vLLM — only in the
unmerged PR [vllm#45163](https://github.com/vllm-project/vllm/pull/45163)
(branch `dgemma`). A lean overlay of just the PR's 41 `vllm/*.py` files
**version-skews** on a stock nightly: load-bearing dgemma changes live in files
*outside* the PR diff (e.g. `build_attn_metadata()`'s `causal` kwarg in
`v1/worker/gpu/attn_utils.py`), so a PR-only overlay dies at boot with
`build_attn_metadata() got an unexpected keyword argument 'causal'`.

So this overlay is the **complete stock-nightly-vs-dgemma-branch `vllm/` delta**
(the 123 differing `.py` files — ADD + CHG), which exactly reproduces the
validated branch `vllm/` tree on top of the pinned nightly. Files identical
between stock and branch are *not* vendored (the stock copies are correct).

## The 3 Codex-authored files (NOT branch-pristine)

These override the branch versions with our Ampere/TP fixes:

| File | Fix |
|---|---|
| `model_executor/kernels/linear/scaled_mm/marlin.py` | Marlin sub-tile-K pad (dense) — lets fp8 Marlin W8A16 tile K=352/1056 within sm_86's 99 KB shared mem (identical stock==branch otherwise, so it's additive). |
| `model_executor/layers/quantization/utils/marlin_utils_fp8.py` | Marlin sub-tile-K pad (FP8 MoE). |
| `model_executor/models/diffusion_gemma.py` | PR file + Codex's TP-vocab soft-embedding fix (slice probs to the rank's vocab shard → local-embed matmul → TP all-reduce) + the `:656` dtype cast (`.to(sc_embeds.dtype)`). |

## Pinned base + rebase

- **Base image:** `vllm/vllm-openai:nightly-2c9c07c85e56c799afffd5a671a8a0bace377a39`
  (engine profile `vllm-diffusion-gemma` `install.spec`; compose `${VLLM_IMAGE}` default).
- **transformers:** the stock nightly's bundled version suffices — this overlay
  vendors its own `transformers_utils/configs/diffusion_gemma.py`, so no
  `pip install transformers@main` is needed (it was a no-op on this nightly).

**Regenerate on a nightly re-pin** (the base nightly *will* be purged from Docker
Hub eventually — known vLLM-nightly behavior):

1. Build the dgemma branch image (helper Dockerfile in `../dgemma-pr45163/`,
   pin `DGEMMA_SHA`), and pull the NEW stock nightly.
2. Hash both images' `vllm/` `.py` trees (`find -name '*.py' -exec sha256sum`),
   diff the manifests → the ADD+CHG set = the new overlay.
3. Re-apply the 3 Codex files above.
4. Bump the pin in `base.yml` + `engines/vllm-diffusion-gemma.yml`, re-validate
   (boot + serve + the gate), update the learnings file.

**Retire entirely** when vllm#45163 merges into a pinnable nightly/release that
registers `DiffusionGemmaForBlockDiffusion` natively — then this collapses to a
single engine pin with (at most) the marlin-k-pad fixes as a lean overlay.
