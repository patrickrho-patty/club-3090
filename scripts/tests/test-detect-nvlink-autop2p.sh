#!/usr/bin/env bash
# detect_nvlink.sh `auto` mode must auto-enable PCIe P2P when nvidia-smi reports
# P2P=OK between all pairs (a patched consumer-GPU driver on a P2P-capable layout),
# and MUST stay off when P2P is unavailable (stock driver → CNS, or cards on
# separate root complexes). NVLink detection still wins when present.
#
# nvidia-smi is mocked (no real GPUs); FAKE_GPUS / FAKE_LINK / FAKE_P2P drive it.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
DETECT="${ROOT_DIR}/scripts/detect_nvlink.sh"
MOCK_DIR="$(mktemp -d)"
trap 'rm -rf "$MOCK_DIR"' EXIT

cat > "$MOCK_DIR/nvidia-smi" <<'MOCK'
#!/usr/bin/env bash
n="${FAKE_GPUS:-2}"; args="$*"
case "$args" in
  "-L")
    for ((i=0;i<n;i++)); do echo "GPU $i: NVIDIA GeForce RTX 3090 (UUID: GPU-$i)"; done ;;
  "topo -m")
    printf "\t"; for ((j=0;j<n;j++)); do printf "GPU%d\t" "$j"; done; printf "\n"
    for ((i=0;i<n;i++)); do printf "GPU%d\t" "$i"
      for ((j=0;j<n;j++)); do [ "$i" = "$j" ] && printf "X\t" || printf "%s\t" "${FAKE_LINK:-PHB}"; done
      printf "\n"; done ;;
  "topo -p2p r")
    printf "\t"; for ((j=0;j<n;j++)); do printf "GPU%d\t" "$j"; done; printf "\n"
    for ((i=0;i<n;i++)); do printf "GPU%d\t" "$i"
      for ((j=0;j<n;j++)); do
        if [ "$i" = "$j" ]; then printf "X\t"
        elif [ "${FAKE_P2P:-CNS}" = "MIXED" ] && [ "$i" = 0 ] && [ "$j" = 1 ]; then printf "CNS\t"
        else printf "%s\t" "${FAKE_P2P:-CNS}"; fi
      done; printf "\n"; done ;;
esac
exit 0
MOCK
chmod +x "$MOCK_DIR/nvidia-smi"

fail=0
# $1=gpus $2=link $3=p2p -> "DISABLE=<>|LEVEL=<>"
run() {
  PATH="$MOCK_DIR:$PATH" FAKE_GPUS="$1" FAKE_LINK="$2" FAKE_P2P="$3" NVLINK_MODE=auto \
    bash -c "source '$DETECT' >/dev/null 2>&1; printf 'DISABLE=%s|LEVEL=%s' \"\${NCCL_P2P_DISABLE:-}\" \"\${NCCL_P2P_LEVEL:-}\""
}
check() {
  local desc="$1" gpus="$2" link="$3" p2p="$4" want="$5" got
  got="$(run "$gpus" "$link" "$p2p")"
  if [ "$got" != "$want" ]; then echo "[autop2p] FAIL: $desc — got '$got' want '$want'" >&2; fail=1
  else echo "[autop2p] ok: $desc"; fi
}

# 2-GPU, no NVLink, P2P=OK (patched driver, shared root) -> AUTO-ENABLE PCIe P2P
check "2gpu PHB + P2P OK -> enabled@PHB" 2 PHB OK  "DISABLE=|LEVEL=PHB"
# 2-GPU, no NVLink, P2P=CNS (this rig: stock driver / separate root complex) -> OFF
check "2gpu PHB + P2P CNS -> off"        2 PHB CNS "DISABLE=1|LEVEL="
# 2-GPU NVLink present -> NVLink wins (NVL), regardless of P2P matrix
check "2gpu NVLink -> enabled@NVL"       2 NV4 CNS "DISABLE=|LEVEL=NVL"
# >2 GPUs, no NVLink, all pairs OK -> auto-enable
check "4gpu PHB + all P2P OK -> enabled" 4 PHB OK  "DISABLE=|LEVEL=PHB"
# >2 GPUs, one pair NOT OK -> stay off (custom all-reduce needs full P2P)
check "4gpu PHB + mixed P2P -> off"      4 PHB MIXED "DISABLE=1|LEVEL="
# >2 GPUs, no P2P at all -> off
check "4gpu PHB + no P2P -> off"         4 PHB CNS "DISABLE=1|LEVEL="

if [ "$fail" -ne 0 ]; then echo "[autop2p] FAILED" >&2; exit 1; fi
echo "[autop2p] PASS: auto promotes to PCIe P2P only when topo -p2p reports OK on all pairs"
