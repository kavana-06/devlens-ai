from pathlib import Path

from analyzer.python_parser import extract_python_structure


IGNORED_DIRECTORIES = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    "node_modules",
}


def build_dependency_graph(repository_path: str) -> dict[str, list[str]]:
    """
    Build a dependency graph for Python files in a repository.

    Each key represents a Python file.
    Each value contains the Python modules imported by that file.
    """

    root = Path(repository_path)

    if not root.exists():
        raise FileNotFoundError(
            f"Repository path does not exist: {repository_path}"
        )

    if not root.is_dir():
        raise ValueError(
            f"Repository path is not a directory: {repository_path}"
        )

    graph = {}

    for path in root.rglob("*.py"):
        if not path.is_file():
            continue

        if any(
            ignored_directory in path.parts
            for ignored_directory in IGNORED_DIRECTORIES
        ):
            continue

        try:
            source_code = path.read_text(
                encoding="utf-8",
                errors="replace",
            )

            structure = extract_python_structure(
                source_code
            )

        except (OSError, ValueError):
            continue

        relative_path = path.relative_to(root).as_posix()

        graph[relative_path] = [
            import_info["name"]
            for import_info in structure["imports"]
        ]

    return graph