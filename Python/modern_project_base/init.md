# Modern Python Base Project Explained

This document explains the structure and tooling of this base project (`modern_project_base`). It is configured with current (2024+) best practices for Python development.

## 1. Project Structure

```text
modern_project_base/
├── pyproject.toml      # The single source of truth for project configuration
├── src/                # Source code directory (src-layout prevents import errors)
│   └── my_package/     # The actual importable package
│       ├── __init__.py
│       └── main.py
└── tests/              # Test suite directory
    └── test_main.py
```

We use the **`src` layout** (putting the package `.py` files under a `src/` folder rather than directly in the root). This is the modern standard because it strictly separates the code being developed from the tool configurations in the root directory, preventing accidental imports of local files during testing.

## 2. Configuration (`pyproject.toml`)

Historically, Python projects required multiple configuration files (`setup.py`, `setup.cfg`, `requirements.txt`, `pytest.ini`, `.flake8`, etc.). 

The `pyproject.toml` file (defined in PEP 518 and PEP 621) replaces almost all of these. It is broken down into specific tables (sections like `[project]`).

### `[project]` Table
Defines the core metadata of the package, including its name, version, authors, and the minimum Python version required (`requires-python = ">=3.11"`).

### `[build-system]` Table
Specifies what tool handles converting your source code into a distributable package (like a `.whl` file). We use **Hatchling** (`hatchling.build`), a modern, fast, and feature-rich build backend that works natively with `pyproject.toml`.

## 3. The Toolchain

We are using a modern, consolidated toolchain focusing on speed and strictness.

### Package Management: `uv`
While not explicitly written in the `pyproject.toml` (as `uv` is an external tool), this project is designed to be used with Astral's `uv`.
- **What it is:** A Python package installer and resolver written in Rust.
- **Why use it:** It is a drop-in replacement for `pip` and `pip-tools`, but it routinely executes 10x to 100x faster. 
- **Usage:** Instead of `pip install pytest`, you run `uv pip install pytest`. You can also use `uv venv` to create virtual environments instantly.

### Linter and Formatter: `ruff`
Configured under the `[tool.ruff]` section.
- **What it is:** An extremely fast Python linter and code formatter, also written in Rust (by Astral).
- **Why use it:** It replaces dozens of older tools (`flake8`, `black`, `isort`, `pydocstyle`, etc.) with a single, unified, lightning-fast executable.
- **Configuration highlights:**
  - `target-version = "py311"`: Ensures Ruff formats code using Python 3.11 features.
  - `select = ["E", "F", "I", "UP", "B", "SIM"]`: We enable standard errors/warnings (`E`, `F`), `isort` for import sorting (`I`), `pyupgrade` for modernizing syntax (`UP`), `flake8-bugbear` for finding likely bugs (`B`), and `flake8-simplify` (`SIM`).
  - `fixable = ["ALL"]`: Allows `ruff check --fix` to automatically correct most issues.

### Testing: `pytest`
Configured under the `[tool.pytest.ini_options]` section.
- **What it is:** The standard framework for testing Python code.
- **Why use it:** It has a simple syntax (`assert x == y` instead of complex `unittest` boilerplate) and a massive ecosystem of plugins.
- **Configuration highlights:**
  - `addopts = "-ra -q --cov=my_package"`: Automatically runs with coverage reporting enabled (`pytest-cov`), prints a short summary (`-ra`), and keeps standard output quiet (`-q`).
  - `testpaths = ["tests"]`: Tells pytest exactly where to look for tests.

### Static Type Checking: `mypy`
Configured under the `[tool.mypy]` section.
- **What it is:** A static type checker for Python.
- **Why use it:** By adding type hints (e.g., `def greet(name: str) -> str:`), `mypy` can catch `TypeError`s and `AttributeError`s before you even run the code.
- **Configuration highlights:**
  - `strict = true`: Enables all strictness flags. This forces you to write fully typed code, preventing creeping technical debt in larger projects.
  - `warn_return_any = true`: Warns if a function returns an `Any` type when it shouldn't.
