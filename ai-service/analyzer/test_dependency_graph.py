from pathlib import Path

from analyzer.dependency_graph import build_dependency_graph


def test_build_dependency_graph(tmp_path: Path):
    services_directory = tmp_path / "services"
    services_directory.mkdir()

    user_service = services_directory / "user_service.py"

    user_service.write_text(
        """
from repositories.user_repository import UserRepository
from models.user import User


class UserService:
    pass
"""
    )

    repository_directory = tmp_path / "repositories"
    repository_directory.mkdir()

    user_repository = repository_directory / "user_repository.py"

    user_repository.write_text(
        """
import sqlite3


class UserRepository:
    pass
"""
    )

    graph = build_dependency_graph(str(tmp_path))

    assert graph == {
        "repositories/user_repository.py": [
            "sqlite3",
        ],
        "services/user_service.py": [
            "repositories.user_repository",
            "models.user",
        ],
    }


def test_ignores_virtual_environment(tmp_path: Path):
    venv_directory = tmp_path / ".venv"
    venv_directory.mkdir()

    ignored_file = venv_directory / "ignored.py"
    ignored_file.write_text(
        "import something"
    )

    app_file = tmp_path / "app.py"
    app_file.write_text(
        "import requests"
    )

    graph = build_dependency_graph(str(tmp_path))

    assert "app.py" in graph
    assert ".venv/ignored.py" not in graph


def test_handles_invalid_python(tmp_path: Path):
    broken_file = tmp_path / "broken.py"

    broken_file.write_text(
        """
def broken_function(
"""
    )

    graph = build_dependency_graph(str(tmp_path))

    assert graph == {}


def test_missing_repository_raises_error(tmp_path: Path):
    missing_path = tmp_path / "does-not-exist"

    try:
        build_dependency_graph(str(missing_path))
        assert False
    except FileNotFoundError as exception:
        assert "Repository path does not exist" in str(exception)