"""v0.8.0 Pull-Emit-Derived `[E]` — STEP E3: capability-aware derived smoke
+ the 4 §6 capture-point artifact emitters + the §6.2/§6.3 manifest.

CONTRACT-4 (the brief's locked E3 spec, capture half). `[E]` **emits** these;
`[F]` (the Loop — §6.1 classifier / §6.2 inbound-trust / §6.3 dedup /
consensus / promotion) **consumes** them and is explicitly OUT of scope here.

This module owns ONLY:
  * `smoke_derived()`  — the capability-aware DERIVED smoke prober
                         (CONTRACT-4 "Capability-smoke set for DERIVED
                         models" — the conservative floor);
  * `emit_capture()`   — write the 4 §6 capture-point artifacts (pt1 gate /
                         pt2 download / pt3 boot / pt4 smoke) + a top-level
                         `manifest.json`, schema **v1**, redacted via the
                         `report.sh --redact` convention.

CAPTURE-POINT 5 (override-accepted force-capture) is the ONE additive E4
extension to this module (`emit_override_capture()` — §5.3 / CONTRACT-4
pt5). It is emitted ONLY on the post-`[C1]` override-accepted path E4
wires; the E3 pt1-4 + manifest emitters below are byte-behaviour-preserving
(`test-pullemit-capture.sh` stays green — it asserts pt5 is NOT written by
`emit_capture()`; pt5 is a SEPARATE function E4 invokes only when
`einput.is_override_accepted`). NO `run_pull()` wiring here (that is E4).
NO §6.1 failure classification (`failure_class` is left null — that is
`[F]`'s job). NO docs (E5). NO real on-rig boot (E5).
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from .downloader import sanitize_slug

SCHEMA = 1

# ---------------------------------------------------------------------------
# CONTRACT-4 capability-smoke set for DERIVED models.
#
# A derived generic profile declares no capabilities, so the conservative
# floor is: plain-chat ALWAYS + streaming ALWAYS (cheap; catches the #145
# class — a model can boot + answer plain chat while streaming/tools/etc are
# silently dead). The remaining capabilities are smoked ONLY if `der`'s
# config.json POSITIVELY declares them; otherwise recorded "unsmoked" and
# the anchor is `partial` (per §6.2: an anchor with un-smoked capabilities
# is `partial` and cannot graduate to Tier-1 for those capabilities).
# ---------------------------------------------------------------------------
FLOOR_CAPS = ("plain-chat", "streaming")
OPTIONAL_CAPS = (
    "tool-call",
    "reasoning-streaming",
    "structured-output",
    "vision",
    "long-context",
)


@dataclass
class SmokeResult:
    smoke_capability_set: list[str] = field(default_factory=list)
    # {<cap>: "green" | "red" | "unsmoked"}
    results: dict[str, str] = field(default_factory=dict)
    partial: bool = False


def _config_declares(der: Any, cap: str) -> bool:
    """Does `der`'s config.json POSITIVELY declare `cap`?

    A derived generic-dense model surfaces config.json signals on
    `der.profile`. We read ONLY positive declarations (never infer a
    capability from absence). The recognised positive signals, conservative
    by design (unknown -> not declared -> "unsmoked" -> partial):

      tool-call           config.json declares a tool/function-calling
                          chat-template or `tool_use`/`tools` support, OR
                          the deriver surfaced a positive tool flag.
      reasoning-streaming config declares a reasoning/thinking parser
                          (`reasoning`/`thinking` config block).
      structured-output   config declares guided/structured-output support.
      vision              an image/vision config block, a *VL/*Vision
                          architecture, or a positive vision flag.
      long-context        config declares a context window beyond the
                          plain-floor (e.g. `max_position_embeddings` /
                          `rope_scaling`) AND the runtime selected a large
                          max_model_len — derived defers this unless the
                          model itself positively declares it.

    `der.profile` may carry a raw config dict under `config`/`_config`
    (whatever the deriver/orchestrator attaches); we look there + at the
    surfaced `arch`. We NEVER mutate the deriver and NEVER guess.
    """
    prof = getattr(der, "profile", None) or {}
    cfg = prof.get("config") or prof.get("_config") or {}
    arch = str(prof.get("arch") or "").lower()

    def has(*keys: str) -> bool:
        return any(k in cfg and cfg.get(k) for k in keys)

    if cap == "tool-call":
        return bool(
            prof.get("supports_tool_call") is True
            or has("tool_use", "tools", "function_calling")
            or (isinstance(cfg.get("chat_template"), str)
                and "tool" in cfg["chat_template"].lower())
        )
    if cap == "reasoning-streaming":
        return bool(
            prof.get("supports_reasoning") is True
            or has("reasoning", "thinking", "reasoning_parser")
        )
    if cap == "structured-output":
        return bool(
            prof.get("supports_structured_output") is True
            or has("guided_decoding", "structured_outputs", "grammar")
        )
    if cap == "vision":
        return bool(
            prof.get("supports_vision") is True
            or has("vision_config", "image_token_id", "vision_tower")
            or arch.endswith(("vl", "vision"))
            or "vl" in arch
            or "vision" in arch
        )
    if cap == "long-context":
        return bool(
            prof.get("supports_long_context") is True
            or has("rope_scaling")
        )
    return False


def smoke_derived(
    einput, endpoint: str, *, client: Optional[Any] = None
) -> SmokeResult:
    """Capability-aware DERIVED smoke prober (CONTRACT-4).

    The DERIVED floor: **plain-chat ALWAYS + streaming ALWAYS** (cheap;
    catches the #145 class). `tool-call` / `reasoning-streaming` /
    `structured-output` / `vision` / `long-context` are probed ONLY if
    `der`'s config.json positively declares them; otherwise recorded
    `"unsmoked"`. `partial = any(v == "unsmoked")` — per §6.2 an anchor
    with un-smoked capabilities is `partial` and cannot graduate to Tier-1
    for those capabilities.

    `client` is INJECTABLE: default = the real OpenAI-compatible probe
    against `endpoint`; E3 tests pass a fixture client so there is NO live
    server in CI. A client must provide:
      .probe(capability, endpoint) -> bool   (True == green)
    """
    if client is None:
        client = _HttpSmokeClient()

    der = einput.der
    probe_set: list[str] = list(FLOOR_CAPS)
    for cap in OPTIONAL_CAPS:
        if _config_declares(der, cap):
            probe_set.append(cap)

    results: dict[str, str] = {}
    # FLOOR + declared caps -> actually probed; everything in OPTIONAL_CAPS
    # not declared -> "unsmoked" (recorded, drives `partial`).
    for cap in FLOOR_CAPS + OPTIONAL_CAPS:
        if cap in probe_set:
            try:
                ok = bool(client.probe(cap, endpoint))
            except Exception:
                ok = False
            results[cap] = "green" if ok else "red"
        else:
            results[cap] = "unsmoked"

    partial = any(v == "unsmoked" for v in results.values())
    return SmokeResult(
        smoke_capability_set=sorted(probe_set),
        results=results,
        partial=partial,
    )


class _HttpSmokeClient:
    """Real probe client (NOT exercised in E3 CI — a fixture client is
    injected; the live server is E5 on-rig). Codifies the minimal
    OpenAI-compatible probe per capability so E5 has nothing to invent."""

    def probe(self, capability: str, endpoint: str) -> bool:  # pragma: no cover - E5
        import urllib.error
        import urllib.request

        url = f"{endpoint}/chat/completions"
        body = {
            "model": "derived",
            "messages": [{"role": "user", "content": "ping"}],
            "max_tokens": 8,
        }
        if capability == "streaming":
            body["stream"] = True
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(body).encode(),
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.status == 200
        except (urllib.error.URLError, OSError):
            return False


# ---------------------------------------------------------------------------
# Redaction — REUSE the `report.sh --redact` convention (do NOT reinvent).
#
# report.sh's `redact()` (scripts/report.sh:66-80) is a bash sed pipeline; it
# is not independently importable, so E3 reuses the SAME convention by
# applying the IDENTICAL sed expression set, driven by the SAME env keys
# (USER / hostname / HF token). Kept in lock-step with report.sh:66-80 — if
# that block changes, this must change with it. No path/token/host leak.
# ---------------------------------------------------------------------------
def _redact_text(text: str) -> str:
    user = os.environ.get("USER") or ""
    try:
        host = subprocess.run(
            ["hostname", "-s"], capture_output=True, text=True, check=False
        ).stdout.strip()
    except Exception:  # pragma: no cover - hostname always present on rig
        host = ""

    # The EXACT report.sh:66-80 expression set (verbatim convention reuse).
    sed_exprs: list[str] = []
    if user:
        sed_exprs += ["-e", f"s|/home/{re.escape(user)}|~|g"]
    sed_exprs += ["-e", "s|/root|~|g"]
    if host:
        sed_exprs += ["-e", f"s|{re.escape(host)}|<HOST>|g"]
    if user:
        sed_exprs += ["-e", f"s|{re.escape(user)}|<USER>|g"]
    sed_exprs += [
        "-e", 's|HF_TOKEN=[^ "]*|HF_TOKEN=<REDACTED>|g',
        "-e", 's|HUGGING_FACE_HUB_TOKEN=[^ "]*|HUGGING_FACE_HUB_TOKEN=<REDACTED>|g',
        "-e", 's|api_key=[^ "]*|api_key=<REDACTED>|gi',
        "-e", r's|hf_[A-Za-z0-9]\{30,\}|hf_<REDACTED>|g',
    ]
    # Hardening BEYOND report.sh's home/root convention (additive, never
    # weaker): the CONTRACT-4 schema carries only slugs / verdicts /
    # relative filenames — it must NEVER carry an absolute internal host
    # path. report.sh only collapses ~/  + /root; a capture artifact is
    # consumed by [F]/cross-rig so ANY absolute internal mount path
    # (/opt/* /mnt/* /data/*) is scrubbed to <PATH> as a defence in depth
    # (the "don't leak internal paths in public artifacts" stack rule).
    sed_exprs += [
        "-e", r's|/opt/[A-Za-z0-9._/-]*|<PATH>|g',
        "-e", r's|/mnt/[A-Za-z0-9._/-]*|<PATH>|g',
        "-e", r's|/data/[A-Za-z0-9._/-]*|<PATH>|g',
    ]
    try:
        proc = subprocess.run(
            ["sed", *sed_exprs],
            input=text, capture_output=True, text=True, check=True,
        )
        return proc.stdout
    except Exception:  # pragma: no cover - sed is POSIX-ubiquitous
        return text


def _write_redacted_json(path: Path, obj: dict) -> None:
    raw = json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False)
    path.write_text(_redact_text(raw) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# §6.2 submission_fingerprint + manifest helpers.
# ---------------------------------------------------------------------------
def _fingerprint(parts: list[str]) -> str:
    h = hashlib.sha256()
    h.update("\x1f".join(str(p) for p in parts).encode("utf-8"))
    return h.hexdigest()


def _arch_family(der: Any) -> Optional[str]:
    prof = getattr(der, "profile", None) or {}
    return prof.get("arch") or prof.get("family")


def _quant_label(der: Any) -> Optional[str]:
    prof = getattr(der, "profile", None) or {}
    return prof.get("weight_format")


def _topology_class(einput) -> str:
    """A coarse, deterministic class for §6.2/§6.3 (NOT the canonical
    summary — that is `topology_summary_canonical`). N GPUs × VRAM-bucket."""
    n = len(einput.selected_gpu_vram_mib or [])
    vram = min(einput.selected_gpu_vram_mib) if einput.selected_gpu_vram_mib else 0
    return f"{n}x{vram}MiB"


# ---------------------------------------------------------------------------
# THE 4 §6 capture-point emitters + manifest.
# ---------------------------------------------------------------------------
def emit_capture(
    einput,
    *,
    confidence,
    raw_verdict,
    profile_like: str,
    download_result,
    boot_result,
    smoke_result: SmokeResult,
    compose_meta: dict,
    kv_calc_version: str,
    repo_root: Path,
    ts: Optional[str] = None,
) -> dict:
    """Write the 4 §6 capture-point artifacts (pt1 gate / pt2 download /
    pt3 boot / pt4 smoke) + a top-level `manifest.json`, schema v1, JSON,
    redacted via the `report.sh --redact` convention, under:

        <repo>/.pull-captures/<slug-sanitized>/<utc-ts>/

    Returns `{paths:{...}, dir:str, manifest:{...}}`. CONTRACT-4 EXACTLY:
      pt1 gate     {schema, point, slug, confidence, raw_verdict, terminal,
                    profile_like, hardware_sm}
      pt2 download {point, ok, files, bytes, sha_verified, failure}
      pt3 boot     {point, ok, seconds, failure}
      pt4 smoke    {point, smoke_capability_set, results, partial}

    CAPTURE-POINT 5 (override-accepted force-capture) is OUT of E3 scope —
    NOT emitted here (E4 wires it). `failure_class` is left **null** — E3
    must NOT classify (§6.1 = `[F]`'s job).
    """
    san = sanitize_slug(einput.slug)
    stamp = ts or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = Path(repo_root) / ".pull-captures" / san / stamp
    out_dir.mkdir(parents=True, exist_ok=True)

    # ---- pt1: pre-download gate verdict --------------------------------
    pt1 = {
        "schema": SCHEMA,
        "point": "gate",
        "slug": einput.slug,
        "confidence": str(getattr(confidence, "name", confidence)),
        "raw_verdict": raw_verdict,
        "terminal": einput.terminal,
        "profile_like": profile_like,
        "hardware_sm": einput.hardware_sm,
    }

    # ---- pt2: download (the E2 DownloadResult shape) -------------------
    pt2 = {
        "point": "download",
        "ok": bool(getattr(download_result, "ok", False)),
        "files": list(getattr(download_result, "files", []) or []),
        "bytes": int(getattr(download_result, "bytes", 0) or 0),
        "sha_verified": bool(getattr(download_result, "sha_verified", False)),
        "failure": getattr(download_result, "failure", None),
    }

    # ---- pt3: boot -----------------------------------------------------
    pt3 = {
        "point": "boot",
        "ok": bool(getattr(boot_result, "ok", False)),
        "seconds": float(getattr(boot_result, "seconds", 0.0) or 0.0),
        "failure": getattr(boot_result, "failure", None),
    }

    # ---- pt4: post-boot capability-aware smoke ------------------------
    pt4 = {
        "point": "smoke",
        "smoke_capability_set": list(smoke_result.smoke_capability_set),
        "results": dict(smoke_result.results),
        "partial": bool(smoke_result.partial),
    }

    # ---- manifest: §6.2 consensus-key inputs as FIRST-CLASS fields -----
    # (Codex-r5 High-2 — [F] must reason OVER them; a hash is opaque.)
    model = einput.slug
    quant_label = _quant_label(einput.der)
    arch_family = _arch_family(einput.der)
    topology_class = _topology_class(einput)
    engine_pin = compose_meta.get("resolved_image") or compose_meta.get(
        "engine_pin"
    )
    engine_version = engine_pin
    selected_ctx = compose_meta.get("max_model_len")
    kv_format = compose_meta.get("kv_format")
    smoke_capability_set = list(smoke_result.smoke_capability_set)
    topology_summary_canonical = einput.topology_summary

    outcome = (
        "smoke-green"
        if (pt3["ok"] and not smoke_result.partial
            and all(v == "green" for v in smoke_result.results.values()
                    if v != "unsmoked"))
        else "partial-or-failed"
    )
    submission_fingerprint = _fingerprint([
        model,
        einput.club3090_commit,
        topology_summary_canonical,
        str(quant_label),
        kv_calc_version,
        str(engine_version),
        stamp,
        outcome,
    ])

    manifest = {
        "schema": SCHEMA,
        "slug": einput.slug,
        "utc_ts": stamp,
        # §6.2 stage-2 hash (quick correlation).
        "submission_fingerprint": submission_fingerprint,
        # §6.2 consensus-key inputs — FIRST-CLASS (not only hashed).
        "model": model,
        "quant_label": quant_label,
        "arch_family": arch_family,
        "topology_class": topology_class,
        "engine_pin": engine_pin,
        "engine_version": engine_version,
        "kv_calc_version": kv_calc_version,
        "selected_ctx": selected_ctx,
        "kv_format": kv_format,
        "smoke_capability_set": smoke_capability_set,
        # §6.2 verbatim — sorted (gpu_name, vram_mib) serialization.
        "topology_summary_canonical": topology_summary_canonical,
        # §6.3 dedup-key inputs — FIRST-CLASS too. `[E]` emits the inputs;
        # `[F]` computes/uses the key. `failure_class` is left **null**:
        # that is §6.1 classifier = `[F]`'s job; E3 must NOT classify.
        "model_id": model,
        "failure_class": None,
        "club3090_commit": einput.club3090_commit,
        "outcome": outcome,
        "capture_points": ["gate", "download", "boot", "smoke"],
    }

    paths = {
        "gate": str(out_dir / "pt1-gate.json"),
        "download": str(out_dir / "pt2-download.json"),
        "boot": str(out_dir / "pt3-boot.json"),
        "smoke": str(out_dir / "pt4-smoke.json"),
        "manifest": str(out_dir / "manifest.json"),
    }
    _write_redacted_json(Path(paths["gate"]), pt1)
    _write_redacted_json(Path(paths["download"]), pt2)
    _write_redacted_json(Path(paths["boot"]), pt3)
    _write_redacted_json(Path(paths["smoke"]), pt4)
    _write_redacted_json(Path(paths["manifest"]), manifest)

    return {"paths": paths, "dir": str(out_dir), "manifest": manifest}


# ---------------------------------------------------------------------------
# CAPTURE-POINT 5 — override-accepted force-capture (CONTRACT-4 pt5 / §5.3).
#
# ADDITIVE E4 extension (NOT invoked by emit_capture(); a SEPARATE function
# E4 calls ONLY on the post-`[C1]` override-accepted path, i.e. when
# `einput.is_override_accepted` is True). E3's pt1-4 + manifest emitters
# above are byte-behaviour-preserving — `test-pullemit-capture.sh` continues
# to assert `emit_capture()` writes ONLY pt1-4 + manifest and NO override
# artifact. pt5 is written into the SAME `<repo>/.pull-captures/<slug>/<ts>/`
# directory, redacted via the SAME convention, schema-less per CONTRACT-4
# pt5's literal field list.
#
# CONTRACT-4 pt5 / §5.3 — emit EXACTLY:
#   { point:"override_capture",
#     predicted_b_breakdown:{ the full [B] kv-calc GB breakdown that
#                             produced the verdict },
#     actual:{ boot_peak_mib:int|null, gpu_worker_reported_mib:int|null },
#     predicted_vs_actual_delta_mib:int|null,
#     exit_error_summary:str|null,
#     calibration_signal_not_validated:true }
# The `true` flag is MANDATORY + LITERAL — §5.3: a forced low-confidence
# download is a calibration SIGNAL, never recorded as fit-validated. `actual`
# may be null (boot never reached allocation) — then `exit_error_summary`
# carries why; the artifact is STILL emitted regardless.
# ---------------------------------------------------------------------------
def emit_override_capture(
    einput,
    *,
    predicted_b_breakdown,
    boot_peak_mib: Optional[int] = None,
    gpu_worker_reported_mib: Optional[int] = None,
    exit_error_summary: Optional[str] = None,
    repo_root: Path,
    ts: str,
) -> str:
    """Write the §5.3 / CONTRACT-4 pt5 override-accepted force-capture
    artifact into the SAME capture directory `emit_capture()` used (keyed by
    the SAME sanitized-slug + `ts`). Returns the written path.

    `predicted_b_breakdown` is the full `[B]` kv-calc GB breakdown that
    produced the verdict (E4 passes `res.diagnostics['b_breakdown']`).
    `actual` is `null` iff BOTH `boot_peak_mib` and
    `gpu_worker_reported_mib` are None (boot never reached allocation) — in
    that case `predicted_vs_actual_delta_mib` is also `null` and
    `exit_error_summary` carries why. `calibration_signal_not_validated` is
    ALWAYS the literal `True` (mandatory; §5.3).
    """
    san = sanitize_slug(einput.slug)
    out_dir = Path(repo_root) / ".pull-captures" / san / ts
    out_dir.mkdir(parents=True, exist_ok=True)

    have_actual = (
        boot_peak_mib is not None or gpu_worker_reported_mib is not None
    )
    if have_actual:
        actual: Optional[dict] = {
            "boot_peak_mib": (
                int(boot_peak_mib) if boot_peak_mib is not None else None
            ),
            "gpu_worker_reported_mib": (
                int(gpu_worker_reported_mib)
                if gpu_worker_reported_mib is not None
                else None
            ),
        }
    else:
        # boot never reached allocation -> actual is null; the WHY lives in
        # exit_error_summary (CONTRACT-4 pt5).
        actual = None

    # predicted_vs_actual_delta_mib: only computable when we have a measured
    # peak AND the prediction carries a comparable MiB figure; else null.
    delta: Optional[int] = None
    if actual is not None and boot_peak_mib is not None:
        pred_mib = _predicted_total_mib(predicted_b_breakdown)
        if pred_mib is not None:
            delta = int(boot_peak_mib) - int(pred_mib)

    pt5 = {
        "point": "override_capture",
        "predicted_b_breakdown": predicted_b_breakdown,
        "actual": actual,
        "predicted_vs_actual_delta_mib": delta,
        "exit_error_summary": exit_error_summary,
        # MANDATORY + LITERAL — never "fit validated" (§5.3).
        "calibration_signal_not_validated": True,
    }
    path = out_dir / "pt5-override-capture.json"
    _write_redacted_json(path, pt5)
    return str(path)


def _predicted_total_mib(breakdown) -> Optional[int]:
    """Best-effort MiB total of the `[B]` GB breakdown (for the
    predicted-vs-actual delta). The `[B]` breakdown is a `{component: GB}`
    dict (`kv.raw_verdict()['breakdown_gb']`); sum numeric components and
    convert GB -> MiB. Returns None if it is not a usable numeric mapping
    (delta stays null — never fabricate a number)."""
    if not isinstance(breakdown, dict) or not breakdown:
        return None
    total_gb = 0.0
    saw = False
    for v in breakdown.values():
        if isinstance(v, (int, float)):
            total_gb += float(v)
            saw = True
    if not saw:
        return None
    return int(round(total_gb * 1024.0))
