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


def module_name_from_path(
    path: Path,
    root: Path,
) -> str:
    """
    Convert a Python file path into its module-style name.

    Example:
        repositories/user_repository.py
        ->
        repositories.user_repository
    """

    relative_path = path.relative_to(root)

    parts = list(relative_path.parts)

    if parts[-1] == "__init__.py":
        parts = parts[:-1]
    else:
        parts[-1] = Path(parts[-1]).stem

    return ".".join(parts)


def find_local_module(
    module_name: str,
    root: Path,
) -> Path | None:
    """
    Find a Python file that matches a module name
    inside the repository.
    """

    module_parts = module_name.split(".")

    module_file = root.joinpath(
        *module_parts
    ).with_suffix(".py")

    if module_file.is_file():
        return module_file

    package_directory = root.joinpath(
        *module_parts
    )

    package_init = package_directory / "__init__.py"

    if package_init.is_file():
        return package_init

    return None


def build_dependency_graph(
    repository_path: str,
) -> dict[str, list[str]]:
    """
    Build a dependency graph for Python files in a repository.

    Each key represents a Python file.

    Each value contains the module names imported
    by that file.
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