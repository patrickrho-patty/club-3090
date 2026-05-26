# CLAUDE.md

Agent guidance for this repository lives in **[AGENTS.md](AGENTS.md)** — read it
first. It's the canonical, engine-agnostic guide: conventions, the compose
`<topology>/<quant>/<serving>.yml` layout, the `compose_registry.py`
single-source-of-truth + `DEFAULTS` resolver, hardware truths, the test pipeline,
and what **not** to do.

**Adding a model?** Start at AGENTS.md → "Adding a model", then follow the full
workflow in **[docs/ADDING_MODELS.md](docs/ADDING_MODELS.md)** (three paths:
serve a safetensors repo via `pull.sh`, run a local GGUF, or promote into the
curated catalog — including the profile-catalog compatibility steps the compose
alone doesn't cover).

> Claude Code reads both `CLAUDE.md` and `AGENTS.md`; this file intentionally
> stays a thin pointer so the two never drift. Put new agent guidance in
> `AGENTS.md`, not here.
