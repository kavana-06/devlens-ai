from pathlib import Path

from git import Repo

from analyzer.git_analyzer import (
    get_changed_files,
    get_commit_count,
    get_current_branch,
    get_latest_commit,
)


def create_test_repository(repository_path: Path) -> Repo:
    """
    Create a temporary Git repository with two commits.
    """

    repository = Repo.init(repository_path)

    readme_file = repository_path / "README.md"
    readme_file.write_text("# DevLens Test Repository")

    repository.index.add(["README.md"])
    repository.index.commit("Initial commit")

    app_file = repository_path / "app.py"
    app_file.write_text("print('Hello DevLens')")

    repository.index.add(["app.py"])
    repository.index.commit("Add application file")

    return repository


def test_get_current_branch(tmp_path: Path):
    repository = create_test_repository(tmp_path)

    branch_name = get_current_branch(str(tmp_path))

    assert branch_name == repository.active_branch.name


def test_get_commit_count(tmp_path: Path):
    create_test_repository(tmp_path)

    commit_count = get_commit_count(str(tmp_path))

    assert commit_count == 2


def test_get_latest_commit(tmp_path: Path):
    repository = create_test_repository(tmp_path)

    latest_commit = get_latest_commit(str(tmp_path))

    assert latest_commit["hash"] == repository.head.commit.hexsha
    assert latest_commit["short_hash"] == repository.head.commit.hexsha[:7]
    assert latest_commit["message"] == "Add application file"
    assert latest_commit["author"]


def test_get_changed_files(tmp_path: Path):
    repository = create_test_repository(tmp_path)

    changed_files = get_changed_files(str(tmp_path))

    assert changed_files == [
        {
            "path": "app.py",
            "change_type": "A",
        }
    ]