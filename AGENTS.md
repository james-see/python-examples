# Agent Guide for `python-examples`

This repository is a collection of small, focused Python examples. It is not a
published Python package; individual files are meant to be copied or adapted.

## Navigation

- Examples are in `python-examples/`.
- File names use `-example.py`.
- Shared boilerplate may live in `python-examples/main.py`, `useragents.py`, or `src/` inside the script.
- Data and fixtures are usually next to the example that uses them.
- Documentation for the Astro site lives in `docs/`.

## Run examples

```sh
uv run python python-examples/requests-example.py
```

or activate the environment first:

```sh
uv sync
source .venv/bin/activate
python python-examples/requests-example.py
```

## Conventions

- Target Python `>=3.12`.
- Prefer the existing style and imports of the nearest example.
- Keep examples small and one-concept focused.
- Do not add network credentials. Use `.env.example`.
- Prefer `pathlib.Path` for new filesystem code.
- Add comments when an example demonstrates a non-obvious API behavior.
- Make scripts safe to import, especially when rerun by agents.

## Testing

There is no central application test suite. Smoke-test a changed example with:

```sh
python -m py_compile python-examples/<name>-example.py
```

For dependency changes:

```sh
uv lock --check
uv sync
```

## Security and cost

Examples may hit third-party APIs. Do not run them automatically unless the user
explicitly asks, and never commit API keys or tokens.
