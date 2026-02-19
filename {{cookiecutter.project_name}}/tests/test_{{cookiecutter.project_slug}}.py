"""Tests for {{cookiecutter.project_slug}}."""

import pytest

from {{cookiecutter.project_slug}} import greet


def test_greet_returns_greeting() -> None:
    """greet() should return a formatted greeting string."""
    assert greet("World") == "Hello, World!"


def test_greet_with_name() -> None:
    """greet() should include the provided name in the output."""
    assert "Alice" in greet("Alice")


@pytest.mark.parametrize("name", ["Alice", "Bob", "Charlie"])
def test_greet_parametrized(name: str) -> None:
    """greet() should work for any name."""
    result = greet(name)
    assert result.startswith("Hello")
    assert name in result
