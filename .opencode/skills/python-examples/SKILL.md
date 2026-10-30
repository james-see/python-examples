---
name: python-examples
description: Navigate and safely extend the james-see/python-examples repository. Use when a user asks about learning Python libraries, running example scripts, adding a new example, cleaning an example, or adapting one of these scripts.
---

# Python Examples

This repository contains standalone examples for common Python libraries. It is not
a library package; run individual scripts directly.

## Workflow

1. Inspect the target example script before making changes.
2. Check it compiles with `python -m py_compile python-examples/<file>`.
3. Do not run network/API examples unless the user explicitly requests it.
4. Follow `.env.example` for secrets.
5. Add concise, focused examples rather than large multi-concept scripts.
6. Keep dependencies in `pyproject.toml` and `uv.lock` when adding imports.

## Safety

- Never commit API keys, tokens, or personal data.
- Use read-only or throwaway accounts for paid/remote APIs.
- Place scripts that produce large side effects under `python-examples/` with clear warnings.

## Suggested quality checks

```sh
uv run ruff check --fix python-examples
uv run python -m py_compile python-examples/example.py
```
