"""v0.8.0 Pull-Emit-Derived `[E]` — STEP E3: the derived boot stage.

CONTRACT-4 (the brief's locked E3 spec, boot half). This module owns ONLY
the derived-compose BOOT; it does NOT wire into `run_pull()` (E4), does NOT
download (E2 owns that), does NOT emit the §6 capture artifacts (that is
`capture.py`, also E3 but a separate module), does NOT do a real on-rig boot
(E5), does NOT write docs (E5).

Boot discipline (the proven on-rig `[D]`/Pull-Gate lesson — reused here)
-----------------------------------------------------------------------
A derived compose boots ONLY with:

  * `docker compose --project-directory <dir> -f <compose> up`  (the
    `--project-directory` discipline — relative volume/path resolution is
    project-dir-relative);
  * the model weights bind-mounted from the HF_HOME host dir
    `<hf_home>/club3090/pulls/<slug-sanitized>/` to the container path
    `/models/club3090/pulls/<slug-sanitized>` — which is EXACTLY the
    `host:container:ro` volume E1's `generate_from_profile()` already emits
    in `compose_text`. It is **NOT** `MODEL_DIR=/mnt/models` (that is the
    curated Path-A convention; a DERIVED model's weights live under HF_HOME,
    per CONTRACT-2 / CONTRACT-3).

`runner` is INJECTABLE. The default runner shells the real `docker compose`;
E3 tests pass a fixture runner so there is NO real Docker / GPU in CI (the
real boot is E5, on-rig). Whatever happens, the boot is ALWAYS torn down on
exit (mirrors the Pull-Gate on-rig harness "always teardown" rule — no
orphaned container/project state, ever).

Public API (stable for E4)
--------------------------

    from scripts.lib.profiles import booter

    res = booter.boot_derived(einput, compose_text, *, runner=None)
    #   res: BootResult
    #     .ok       -> bool
    #     .seconds  -> float            (wall time of the up->ready probe)
    #     .failure  -> None | "<container-died-reason>"
    #     .endpoint -> str | None       (the OpenAI-compatible base URL when
    #                                    ok; None on failure)

`BootResult` IS the §6 capture-point-3 payload source (`capture.py` maps it
to the `{point:"boot", ok, seconds, failure}` artifact — note `endpoint` is
runtime-only plumbing for the smoke prober and is NOT part of the redacted
artifact).
"""

from __future__ import annotations

import shutil
import subprocess
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

from .downloader import sanitize_slug

# The container-side port the derived-vllm template binds (E1 emits
# `... :8000` and `vllm serve --port 8000` inside the container). The host
# port is the compose `${PORT:-<default_port>}`; for the boot readiness probe
# E3 talks to the host-published port carried on einput.runtime.
_CONTAINER_PORT = 8000
_DEFAULT_READY_TIMEOUT_S = 600  # generous; a fixture runner returns instantly


@dataclass
class BootResult:
    ok: bool
    seconds: float = 0.0
    # None on success; a short "<container-died-reason>" string on failure
    # (E3 does NOT classify into §6.1 classes — that is [F]'s job; this is
    # just the raw reason the runner surfaced).
    failure: Optional[str] = None
    # The OpenAI-compatible base URL the smoke prober talks to (ok only).
    endpoint: Optional[str] = None


# ---------------------------------------------------------------------------
# Runner abstraction (injectable; default = real `docker compose`).
#
# A runner must provide:
#   .up(project_dir, compose_path)   -> None
#       bring the derived compose up (the proven `docker compose
#       --project-directory <project_dir> -f <compose_path> up -d` shape).
#       Raise BootError(reason) if the container dies / never becomes ready.
#   .wait_ready(endpoint)            -> None
#       block until the server answers (a cheap GET on the OpenAI base) or
#       raise BootError(reason) on container death / timeout.
#   .down(project_dir, compose_path) -> None
#       tear the compose down (ALWAYS called from boot_derived's finally).
#
# E3 tests inject a fixture runner (no Docker). The real runner is below.
# ---------------------------------------------------------------------------
class BootError(RuntimeError):
    """The runner raises this with a short container-died reason; the stage
    maps it to BootResult.failure and ALWAYS tears down."""


class DockerComposeRunner:
    """Real runner. `docker compose --project-directory <dir>` discipline.

    NOT exercised in E3 CI (a fixture runner is injected — no Docker/GPU in
    unit tests). The real boot is E5, on-rig. This codifies the EXACT
    proven shape so E5 has nothing to invent."""

    ready_timeout_s = _DEFAULT_READY_TIMEOUT_S

    def _compose(self, project_dir: str, compose_path: str, *args: str) -> None:
        cmd = [
            "docker", "compose",
            "--project-directory", project_dir,
            "-f", compose_path,
            *args,
        ]
        proc = subprocess.run(
            cmd, capture_output=True, text=True, check=False
        )
        if proc.returncode != 0:
            tail = (proc.stderr or proc.stdout or "").strip().splitlines()
            reason = tail[-1] if tail else f"exit {proc.returncode}"
            raise BootError(f"docker compose {args[0]} failed: {reason}")

    def up(self, project_dir: str, compose_path: str) -> None:
        self._compose(project_dir, compose_path, "up", "-d")

    def wait_ready(self, endpoint: str) -> None:
        import urllib.error
        import urllib.request

        deadline = time.monotonic() + self.ready_timeout_s
        url = f"{endpoint}/models"
        while time.monotonic() < deadline:
            try:
                with urllib.request.urlopen(url, timeout=5) as resp:
                    if resp.status == 200:
                        return
            except (urllib.error.URLError, OSError):
                pass
            time.sleep(3)
        raise BootError("server did not become ready before timeout")

    def down(self, project_dir: str, compose_path: str) -> None:
        # Best-effort teardown; never raise out of teardown.
        try:
            self._compose(
                project_dir, compose_path, "down", "-v", "--remove-orphans"
            )
        except BootError:
            pass


# ---------------------------------------------------------------------------
# THE boot stage.
# ---------------------------------------------------------------------------
def boot_derived(
    einput, compose_text: str, *, runner: Optional[Any] = None
) -> BootResult:
    """Bring up the E1-emitted derived `compose_text` using the proven
    `docker compose --project-directory` discipline against the HF_HOME
    host->container `:ro` mount E1 already wrote into `compose_text` (NOT
    `MODEL_DIR`).

    The compose is written to a fresh project directory; `runner.up` /
    `runner.wait_ready` are invoked; on success the OpenAI-compatible
    endpoint is returned for the smoke prober. **The boot is ALWAYS torn
    down (runner.down) in a finally**, success or failure — no orphaned
    container/project state (the Pull-Gate on-rig harness lesson).

    Returns `BootResult` (== the §6 capture-point-3 payload source).
    `runner` is injectable: default = real `docker compose`; E3 tests pass a
    fixture runner so there is NO real Docker / GPU in CI.
    """
    if runner is None:
        runner = DockerComposeRunner()

    slug = einput.slug
    san = sanitize_slug(slug)
    rt = einput.runtime or {}
    host_port = int(rt.get("default_port") or rt.get("port") or _CONTAINER_PORT)
    endpoint = f"http://127.0.0.1:{host_port}/v1"

    # Fresh, isolated project directory — the `--project-directory`
    # discipline resolves the compose's relative paths against THIS dir;
    # the derived compose's volume is an ABSOLUTE host HF_HOME path
    # (`<hf_home>/club3090/pulls/<san>:/models/...:ro`, emitted by E1), so
    # the bind mount is the HF_HOME weights dir — never MODEL_DIR.
    project_dir = tempfile.mkdtemp(prefix=f"club3090-derived-{san}-")
    compose_path = str(Path(project_dir) / "docker-compose.yml")
    Path(compose_path).write_text(compose_text, encoding="utf-8")

    started = time.monotonic()
    try:
        runner.up(project_dir, compose_path)
        runner.wait_ready(endpoint)
    except BootError as exc:
        return BootResult(
            ok=False,
            seconds=round(time.monotonic() - started, 3),
            failure=str(exc) or "container died (no reason surfaced)",
            endpoint=None,
        )
    except Exception as exc:  # pragma: no cover - defensive; runner contract
        return BootResult(
            ok=False,
            seconds=round(time.monotonic() - started, 3),
            failure=f"unexpected boot error: {exc!r}",
            endpoint=None,
        )
    else:
        return BootResult(
            ok=True,
            seconds=round(time.monotonic() - started, 3),
            failure=None,
            endpoint=endpoint,
        )
    finally:
        # ALWAYS teardown — mirror the Pull-Gate on-rig harness. Never leave
        # an orphaned container/project; never let teardown raise.
        try:
            runner.down(project_dir, compose_path)
        except Exception:  # pragma: no cover - teardown must never raise
            pass
        shutil.rmtree(project_dir, ignore_errors=True)
