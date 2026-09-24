from pathlib import Path

from git import InvalidGitRepositoryError, Repo


def open_repository(repository_path: str) -> Repo:
    """
    Open a Git repository from the given path.
    """

    path = Path(repository_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Repository path does not exist: {repository_path}"
        )

    if not path.is_dir():
        raise ValueError(
            f"Repository path is not a directory: {repository_path}"
        )

    try:
        return Repo(
            path,
            search_parent_directories=True,
        )
    except InvalidGitRepositoryError as exception:
        raise ValueError(
            f"Directory is not a Git repository: {repository_path}"
        ) from exception


def get_current_branch(repository_path: str) -> str:
    """
    Return the current Git branch name.
    """

    repository = open_repository(repository_path)

    return repository.active_branch.name


def get_commit_count(repository_path: str) -> int:
    """
    Return the total number of commits in the current branch.
    """

    repository = open_repository(repository_path)

    return sum(1 for _ in repository.iter_commits())


def get_latest_commit(repository_path: str) -> dict:
    """
    Return information about the latest commit.
    """

    repository = open_repository(repository_path)

    commit = repository.head.commit

    return {
        "hash": commit.hexsha,
        "short_hash": commit.hexsha[:7],
        "author": str(commit.author),
        "message": commit.message.strip(),
        "timestamp": commit.committed_datetime.isoformat(),
    }


def get_changed_files(
    repository_path: str,
    commit_hash: str | None = None,
) -> list[dict]:
    """
    Return files changed by a specific commit.

    If no commit hash is supplied, the latest commit is used.
    """

    repository = open_repository(repository_path)

    commit = (
        repository.commit(commit_hash)
        if commit_hash
        else repository.head.commit
    )

    if not commit.parents:
        return [
            {
                "path": item.a_path or item.b_path,
                "change_type": item.change_type,
            }
            for item in commit.diff(
                None,
                create_patch=False,
            )
        ]

    parent = commit.parents[0]

    return [
        {
            "path": item.a_path or item.b_path,
            "change_type": item.change_type,
        }
        for item in parent.diff(
            commit,
            create_patch=False,
        )
    ]