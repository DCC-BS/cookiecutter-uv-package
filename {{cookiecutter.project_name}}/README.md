# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

---

<p align="center">
  <a href="https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}">GitHub</a>
  &nbsp;|&nbsp;
  <a href="https://pypi.org/project/{{cookiecutter.project_name}}/">PyPI</a>
</p>

---

[![PyPI version](https://img.shields.io/pypi/v/{{cookiecutter.project_name}}.svg)](https://pypi.org/project/{{cookiecutter.project_name}}/)
[![Python versions](https://img.shields.io/pypi/pyversions/{{cookiecutter.project_name}}.svg)](https://pypi.org/project/{{cookiecutter.project_name}}/)
[![License](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/blob/main/LICENSE)
[![CI](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/actions/workflows/main.yml/badge.svg)](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/actions/workflows/main.yml)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
{% if cookiecutter.codecov == "y" %}[![Coverage](https://codecov.io/gh/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
{% endif %}

## Overview

> TODO: Add a short paragraph describing what this package does and who it is for.

## Requirements

- Python {{cookiecutter.python_version}}+

## Installation

```bash
# with uv (recommended)
uv add {{cookiecutter.project_name}}

# with pip
pip install {{cookiecutter.project_name}}
```

## Usage

```python
from {{cookiecutter.project_slug}} import greet

result = greet("World")
print(result)  # Hello, World!
```

> TODO: Replace the example above with real usage examples for your package.

## API Reference

### `greet(name: str) -> str`

Returns a greeting string.

| Parameter | Type  | Description              |
|-----------|-------|--------------------------|
| `name`    | `str` | The name to greet.       |

**Returns:** `str` – Greeting message.

**Example:**

```python
from {{cookiecutter.project_slug}} import greet

greet("Alice")  # "Hello, Alice!"
```

## Development

### Setup

```bash
git clone https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}.git
cd {{cookiecutter.project_name}}
make install
```

### Available commands

```
make install     Install dependencies and pre-commit hooks
make check       Run all quality checks (ruff lint, format, ty type check)
make test        Run tests with coverage report
make build       Build distribution packages
make publish     Publish to PyPI
```

### Running tests

```bash
make test
```

Tests are in `tests/` and use [pytest](https://pytest.org).
Coverage reports are generated at `coverage.xml` and printed to the terminal.

### Code quality

This project uses:

- **[ruff](https://github.com/astral-sh/ruff)** – linting and formatting
- **[ty](https://github.com/astral-sh/ty)** – type checking
- **[pre-commit](https://pre-commit.com/)** – pre-commit hooks

Run all checks:

```bash
make check
```

### Releasing

Releases are published to PyPI automatically.
Update the version in `pyproject.toml`, then trigger the **Publish** workflow from GitHub Actions:

```
GitHub → Actions → Publish to PyPI → Run workflow
```

The workflow tags the commit, builds the package, and publishes to PyPI via trusted publishing.

## License

[{{cookiecutter.open_source_license}}](LICENSE) © {{cookiecutter.author}}
