"""Post-generation hook: selects the correct license file and cleans up."""

import os
import sys

LICENSE = "{{cookiecutter.open_source_license}}"
CODECOV = "{{cookiecutter.codecov}}"

LICENSE_FILES = {
    "MIT": "LICENSE_MIT",
    "BSD-3-Clause": "LICENSE_BSD",
    "Unlicense": "LICENSE_UNLICENSE",
}


def select_license() -> None:
    """Rename the chosen license file to LICENSE, remove the rest."""
    target = LICENSE_FILES.get(LICENSE)
    if target is None:
        print(f"ERROR: unknown license '{LICENSE}'", file=sys.stderr)  # noqa: T201
        sys.exit(1)

    for name, filename in LICENSE_FILES.items():
        if not os.path.exists(filename):
            continue
        if name == LICENSE:
            os.rename(filename, "LICENSE")
        else:
            os.remove(filename)


def remove_codecov_config() -> None:
    """Remove codecov.yml when codecov integration is not requested."""
    if CODECOV != "y" and os.path.exists("codecov.yml"):
        os.remove("codecov.yml")


if __name__ == "__main__":
    select_license()
    remove_codecov_config()
    print(  # noqa: T201
        "\n✅  Project '{{cookiecutter.project_name}}' generated successfully!\n"
        "\nNext steps:\n"
        "  cd {{cookiecutter.project_name}}\n"
        "  git init\n"
        "  make install\n"
        "  git add .\n"
        "  git commit -m 'chore: initial project scaffold'\n"
        "\nBefore publishing to PyPI:\n"
        "  1. Create the repository on GitHub\n"
        "  2. Push your code\n"
        "  3. Configure PyPI Trusted Publishing for the 'Publish to PyPI' workflow\n"
        "  4. Update the version in pyproject.toml\n"
        "  5. Trigger the 'Publish to PyPI' workflow from GitHub Actions\n"
    )
