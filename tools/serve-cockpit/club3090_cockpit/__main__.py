"""Entry point for the c3 command."""

from __future__ import annotations

import os
import sys
from pathlib import Path


def resolve_surface(argv: list[str], environ: "os._Environ[str] | dict[str, str]") -> str:
    """Resolve the audience surface (R0) from CLI args + env.

    `c3 --contribute` (bare flag) or `C3_SURFACE=producer` opts into the producer
    surface (adds the Bring & Validate lane, R3); anything else → consumer. This
    is an env/CLI opt-in read at startup — the app persists no setting (the
    in-app persisted toggle lands in R4). C3_SURFACE is normalised case- and
    whitespace-insensitively so `Producer`/` producer ` also work.
    """
    if "--contribute" in argv:
        return "producer"
    if environ.get("C3_SURFACE", "").strip().lower() == "producer":
        return "producer"
    return "consumer"


def main() -> None:
    """Launch the serve cockpit TUI."""
    # Resolve repo root from this file's location:
    #   <repo>/tools/serve-cockpit/club3090_cockpit/__main__.py
    #   parents[0] = club3090_cockpit/
    #   parents[1] = serve-cockpit/
    #   parents[2] = tools/
    #   parents[3] = <repo root>
    # Override with C3_REPO_ROOT if installed outside the tree.
    env_root = os.environ.get("C3_REPO_ROOT")
    repo_root = Path(env_root) if env_root else Path(__file__).resolve().parents[3]

    if not (repo_root / "scripts").is_dir():
        print(
            f"Error: club-3090 repo root not found at {repo_root} "
            f"(no scripts/ dir).  Run via the repo tree, or set C3_REPO_ROOT.",
            file=sys.stderr,
        )
        sys.exit(1)

    from .app import CockpitApp

    # Surface (R0): consumer (default) vs producer — see resolve_surface().
    # `c3 --contribute` / C3_SURFACE=producer opt in (read at startup; no setting
    # is written — the in-app persisted toggle arrives in R4). Default keeps the
    # consumer UI clean.
    surface = resolve_surface(sys.argv, os.environ)
    app = CockpitApp(repo_root=repo_root, surface=surface)
    app.run()


if __name__ == "__main__":
    main()
