"""{{cookiecutter.project_description}}"""

__version__ = "0.1.0"


def greet(name: str) -> str:
    """Return a greeting for the given name.

    Args:
        name: The name to greet.

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"
