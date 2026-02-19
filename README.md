# cookiecutter-uv-package

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for Python packages published on PyPI, using modern Astral tooling.

---

## Features

- **[uv](https://github.com/astral-sh/uv)** – dependency management and packaging
- **[ruff](https://github.com/astral-sh/ruff)** – linting and formatting
- **[ty](https://github.com/astral-sh/ty)** – type checking
- **[pytest](https://pytest.org)** – testing with branch coverage reports
- **[pre-commit](https://pre-commit.com/)** – automated code quality hooks
- **GitHub Actions CI** – quality checks via [DCC-BS reusable workflows](https://github.com/DCC-BS/ci-workflows), test matrix with optional Codecov upload
- **PyPI publishing** – `workflow_dispatch`-triggered publish with OIDC trusted publishing, automatic git tagging
- **README** with PyPI, CI, license, and coverage badges + usage example
- **`src/` layout** – package lives in `src/<project_slug>/` with a `py.typed` marker
- **Renovate** – automated dependency update PRs

## Requirements

- Python 3.10+
- [cookiecutter](https://cookiecutter.readthedocs.io/)

```bash
uv tool install cookiecutter
# or
pip install cookiecutter
```

## Usage

```bash
cookiecutter gh:DCC-BS/cookiecutter-uv-package
```

Or from a local clone:

```bash
cookiecutter path/to/cookiecutter-uv-package
```

### Template variables

| Variable               | Default                   | Description                                      |
|------------------------|---------------------------|--------------------------------------------------|
| `project_name`         | `my-python-package`       | PyPI package name (kebab-case)                   |
| `project_slug`         | *(derived)*               | Python import name (snake_case, auto-generated)  |
| `project_description`  | `A Python package.`       | One-line description                             |
| `author`               | `Yanick Schraner`         | Author full name                                 |
| `author_github_handle` | `DCC-BS`                  | GitHub user or organisation                      |
| `email`                | `yanick.schraner@bs.ch`   | Author email                                     |
| `python_version`       | `3.12`                    | Minimum Python version                           |
| `open_source_license`  | `MIT`                     | License (`MIT`, `BSD-3-Clause`, `Unlicense`)     |
| `codecov`              | `y`                       | Include Codecov upload in CI (`y` / `n`)         |

## Generated project structure

```
my-python-package/
├── .github/
│   └── workflows/
│       ├── main.yml        # CI: quality + tests (+ optional codecov)
│       └── publish.yml     # Publish to PyPI via trusted publishing
├── src/
│   └── my_python_package/
│       ├── __init__.py     # Package entry point with example function
│       └── py.typed        # PEP 561 marker
├── tests/
│   ├── __init__.py
│   └── test_my_python_package.py
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── codecov.yml             # (only if codecov = y)
├── LICENSE
├── Makefile
├── pyproject.toml
├── README.md
└── renovate.json
```

## CI overview

```
push / PR to main
       │
       ├─► quality (DCC-BS/ci-workflows python-backend-ci)
       │       └─ make check  (ruff lint + format + ty)
       │
       └─► tests (ubuntu-latest matrix)
               ├─ uv sync
               ├─ pytest --cov --cov-report=xml
               └─ codecov upload  (if enabled)

workflow_dispatch
       └─► publish
               ├─ uv version → create & push git tag
               ├─ uv build
               └─ uv publish  (OIDC trusted publishing)
```

## PyPI trusted publishing setup

Before running the publish workflow for the first time:

1. Go to [pypi.org](https://pypi.org) → your project → **Publishing** → **Add a new publisher**
2. Set:
   - **Owner**: your GitHub user/org
   - **Repository**: your repo name
   - **Workflow name**: `publish.yml`
   - **Environment**: *(leave blank)*
3. Trigger the workflow from **GitHub → Actions → Publish to PyPI → Run workflow**

## License

MIT © DCC Data Competence Center
