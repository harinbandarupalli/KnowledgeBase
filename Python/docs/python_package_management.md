# Python Package Management Guide

Effective package management is crucial for maintaining reproducible and isolated Python projects. This guide covers the most common tools and workflows for managing Python dependencies.

## 1. pip (Pip Installs Packages)
`pip` is the standard package installer for Python, used to install packages from the Python Package Index (PyPI).

### Basic Commands
- **Install a package:** `pip install <package_name>`
- **Install a specific version:** `pip install <package_name>==1.2.3`
- **Upgrade a package:** `pip install --upgrade <package_name>`
- **Uninstall a package:** `pip uninstall <package_name>`
- **List installed packages:** `pip list`
- **Show package details:** `pip show <package_name>`

### Requirements Files
A `requirements.txt` file is used to specify a list of packages and their versions for a project.

- **Generate a requirements file:** `pip freeze > requirements.txt`
  *(Note: This captures exact versions of everything currently installed. For a cleaner file, manually create it with only your top-level dependencies.)*
- **Install from a requirements file:** `pip install -r requirements.txt`

## 2. conda (Package, Dependency and Environment Management)
If you are using Miniforge or Anaconda, `conda` handles both virtual environments and package management. It is particularly good for data science as it manages non-Python dependencies (like C libraries) as well.

### Basic Commands
- **Install a package:** `conda install <package_name>`
- **Install a specific version:** `conda install <package_name>=1.2.3`
- **Update a package:** `conda update <package_name>`
- **Remove a package:** `conda remove <package_name>`
- **List installed packages:** `conda list`

### Environment Files
An `environment.yml` file is the conda equivalent of `requirements.txt`, but it also specifies the Python version and environment name.

- **Export an environment:** `conda env export > environment.yml`
  *(Tip: Use `conda env export --no-builds > environment.yml` for better cross-platform compatibility.)*
- **Create an environment from a file:** `conda env create -f environment.yml`
- **Update an environment from a file:** `conda env update --file environment.yml --prune`

## 3. Modern Package Management: pyproject.toml
The Python ecosystem is moving towards a standardized configuration file called `pyproject.toml` (defined in PEP 518 and PEP 621). This single file replaces `setup.py`, `requirements.txt`, and other configuration files (like `pytest.ini` or `.flake8`).

### Tools utilizing pyproject.toml:

#### A. Poetry
Poetry is a popular tool for dependency management and packaging.
- **Initialize a project:** `poetry init` (creates `pyproject.toml`)
- **Add a dependency:** `poetry add <package_name>` (updates `pyproject.toml` and `poetry.lock`)
- **Add a development dependency:** `poetry add --group dev <package_name>`
- **Install dependencies:** `poetry install` (creates a virtual environment if one doesn't exist and installs from the lock file)
- **Run a command in the environment:** `poetry run python script.py`

#### B. pip-tools
A lighter-weight approach that works well with standard `pip` and `pyproject.toml`.
- Define your dependencies in `pyproject.toml` under `[project.dependencies]`.
- **Generate a pinned requirements file:** `pip-compile pyproject.toml` (creates `requirements.txt`)
- **Sync your environment:** `pip-sync requirements.txt` (installs missing packages and removes unneeded ones)

#### C. uv
`uv` is an extremely fast Python package installer and resolver written in Rust. It serves as a drop-in replacement for standard `pip` commands and `pip-tools` but executes significantly faster.
- **Install a package:** `uv pip install <package_name>`
- **Compile requirements:** `uv pip compile pyproject.toml -o requirements.txt`
- **Sync environment:** `uv pip sync requirements.txt`

## 4. Best Practices Summary
1. **Always use a virtual environment** (via conda, venv, or poetry) for every project.
2. **Never `sudo pip install`** or install packages directly into your base Python installation.
3. **Pin your dependencies** either conditionally (e.g., `requests>=2.25.0`) in your project definition or exactly (e.g., `requests==2.31.0`) in a lock file or `requirements.txt` to ensure reproducible builds.
4. If building modern applications, consider adopting `pyproject.toml` alongside tools like Poetry or `uv` for robust dependency resolution.
