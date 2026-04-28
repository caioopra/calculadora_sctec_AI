# Copilot Instructions

## Commands

```bash
uv run python main.py
uv run python -m pytest
uv run python -m pytest tests/test_calculadora.py::test_somar -v
```

## Architecture

- `src/calculadora.py` is the core module. It keeps each calculator operation as a small pure function, including `dividir`, which raises `ValueError` on division by zero.
- `main.py` is only a demonstration entrypoint. It imports the functions from `src.calculadora` and prints fixed sample operations rather than implementing application logic itself.
- `tests/test_calculadora.py` validates the public behavior of the functions imported from `src.calculadora`, with both happy-path assertions and an explicit edge case for division by zero.
- `pyproject.toml` configures pytest to collect tests from `tests/` and adds the repository root to `pythonpath`, so imports use `from src.calculadora import ...`.

## Conventions

- Use `uv run ...` for Python commands so the local `.venv` is activated automatically.
- Keep names, comments, and user-facing messages in Portuguese.
- Follow the repository's didactic style: direct Python, minimal abstraction, and focused changes without opportunistic refactoring.
- When adding a new calculator operation, implement it in `src/calculadora.py`, expose it from `main.py` if it should appear in the demo output, and extend `tests/test_calculadora.py`.
- New tests should stay in the existing pytest style: simple function-based tests covering the main path and at least one edge case when relevant.
- Commit messages follow Conventional Commits in Portuguese, and branch names use `feature/<nome-curto>` for features and `fix/<nome>` for fixes.
