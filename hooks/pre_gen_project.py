"""Pre-generation hook: validate template inputs before creating the project."""

import re
import sys

PROJECT_NAME = "{{cookiecutter.project_name}}"
PROJECT_SLUG = "{{cookiecutter.project_slug}}"

# project_name must use hyphens (PyPI convention for package names)
if not re.match(r"^[a-z][a-z0-9\-]+$", PROJECT_NAME):
    print(  # noqa: T201
        f"ERROR: project_name '{PROJECT_NAME}' is invalid.\n"
        "  Use lowercase letters, digits, and hyphens only (e.g. 'my-cool-package').\n"
        "  The name must start with a letter."
    )
    sys.exit(1)

# project_slug must use underscores (Python import name convention)
if not re.match(r"^[a-z][a-z0-9_]+$", PROJECT_SLUG):
    print(  # noqa: T201
        f"ERROR: project_slug '{PROJECT_SLUG}' is invalid.\n"
        "  Use lowercase letters, digits, and underscores only."
    )
    sys.exit(1)

if "-" in PROJECT_SLUG:
    print(  # noqa: T201
        f"ERROR: project_slug '{PROJECT_SLUG}' must not contain hyphens.\n"
        "  Hyphens in project_name are automatically converted to underscores."
    )
    sys.exit(1)
