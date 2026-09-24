from pathlib import Path

from analyzer.dependency_graph import (
    build_dependency_graph,
    find_local_module,
)


def test_build_dependency_graph(tmp_path: Path):
    services_directory = tmp_path / "services"
    services_directory.mkdir()

    repositories_directory = tmp_path / "repositories"
    repositories_directory.mkdir()

    models_directory = tmp_path / "models"
    models_directory.mkdir()

    user_service = services_directory / "user_service.py"

    user_service.write_text(
        """
from repositories.user_repository import UserRepository
from models.user import User


class UserService:
    pass
"""
    )

    user_repository = repositories_directory / "user_repository.py"

    user_repository.write_text(
        """
from models.user import User


class UserRepository:
    pass
"""
    )

    user_model = models_directory / "user.py"

    user_model.write_text(
        """
class User:
    pass
"""
    )

    graph = build_dependency_graph(str(tmp_path))

    assert graph == {
        "models/user.py": [],
        "repositories/user_repository.py": [
            "models.user",
        ],
        "services/user_service.py": [
            "repositories.user_repository",
            "models.user",
        ],
    }


def test_finds_local_python_module(tmp_path: Path):
    repositories_directory = tmp_path / "repositories"
    repositories_directory.mkdir()

    user_repository = repositories_directory / "user_repository.py"

    user_repository.write_text(
        """
class UserRepository:
    pass
"""
    )

    result = find_local_module(
        "repositories.user_repository",
        tmp_path,
    )

    assert result == user_repository


def test_returns_none_for_external_module(tmp_path: Path):
    result = find_local_module(
        "sqlite3",
        tmp_path,
    )

    assert result is None


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