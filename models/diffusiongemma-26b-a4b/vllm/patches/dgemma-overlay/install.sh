#!/usr/bin/env bash
# =============================================================================
# DiffusionGemma sideload — applies the vllm#45163 (dgemma) overlay onto a STOCK
# pinned vLLM nightly at container start (delivery_mechanism: install_script).
#
# Replaces the former baked image (vllm-dgemma:pr45163). The base image is now a
# stock, PULLABLE nightly; this script copies the vendored overlay over the
# installed vllm package before the server starts. Idempotent: safe to re-run.
#
# The overlay is the FULL stock-nightly-vs-dgemma-branch delta (the 123 differing
# vllm/*.py files), NOT just PR #45163's formal file set: load-bearing dgemma
# changes (e.g. build_attn_metadata's `causal` kwarg in v1/worker/gpu/attn_utils.py)
# live in files outside the PR diff, so a lean PR-only overlay version-skews
# ("build_attn_metadata() got an unexpected keyword argument 'causal'"). The full
# delta reproduces the validated baked image's vllm/ tree exactly. On top of that
# sit Codex's marlin-k-pad fixes (marlin.py/marlin_utils_fp8.py + the diffusion_gemma.py
# TP-vocab/dtype fixes).
#
# REBASE (when the pinned nightly moves / is purged): re-pin the base nightly in
# the engine profile + compose, then regenerate this dir — diff the dgemma branch's
# vllm/ tree vs the NEW stock nightly (hash both, take ADD+CHG), re-apply the 3
# marlin-k-pad files. See the dir README.
# =============================================================================
set -euo pipefail
OVL_DIR="${DGEMMA_OVERLAY_DIR:-/opt/dgemma-overlay}"
PKG="$(python3 -c 'import vllm, os; print(os.path.dirname(vllm.__file__))')"
echo "[dgemma-overlay] applying overlay from ${OVL_DIR} onto ${PKG}"
( cd "${OVL_DIR}" && find . -type f ! -name 'install.sh' ! -name 'README.md' -print0 \
  | while IFS= read -r -d '' rel; do
      dest="${PKG}/${rel#./}"
      mkdir -p "$(dirname "${dest}")"
      cp -f "${OVL_DIR}/${rel#./}" "${dest}"
    done )
# drop stale bytecode so the overlay .py files are the ones imported
find "${PKG}" -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true
# fail fast if the arch did not register (overlay didn't take)
python3 -c "from vllm.model_executor.models.registry import ModelRegistry as R; \
archs=R.get_supported_archs(); \
assert 'DiffusionGemmaForBlockDiffusion' in archs, 'FAIL: DiffusionGemma arch not registered after overlay'; \
print('[dgemma-overlay] OK: DiffusionGemmaForBlockDiffusion registered')"
