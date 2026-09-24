from pathlib import Path

from analyzer.python_parser import extract_python_structure


IGNORED_DIRECTORIES = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    "target",
    "dist",
    "build",
    ".next",
}


LANGUAGE_BY_EXTENSION = {
    ".py": "Python",
    ".java": "Java",
    ".js": "JavaScript",
    ".jsx": "JavaScript",
    ".ts": "TypeScript",
    ".tsx": "TypeScript",
    ".go": "Go",
    ".rs": "Rust",
    ".cpp": "C++",
    ".c": "C",
    ".cs": "C#",
    ".php": "PHP",
    ".rb": "Ruby",
    ".kt": "Kotlin",
    ".swift": "Swift",
    ".sql": "SQL",
    ".html": "HTML",
    ".css": "CSS",
    ".scss": "SCSS",
    ".json": "JSON",
    ".yaml": "YAML",
    ".yml": "YAML",
    ".xml": "XML",
    ".md": "Markdown",
}


MAX_FILE_SIZE = 1_000_000


def detect_language(path: Path) -> str:
    """
    Determine the programming or markup language from a file extension.
    """

    return LANGUAGE_BY_EXTENSION.get(
        path.suffix.lower(),
        "Unknown",
    )


def is_supported_file(path: Path) -> bool:
    """
    Determine whether DevLens should analyze a file.
    """

    return path.suffix.lower() in LANGUAGE_BY_EXTENSION


def read_file_content(path: Path) -> str:
    """
    Read a text file safely using UTF-8 encoding.
    """

    try:
        return path.read_text(
            encoding="utf-8",
            errors="replace",
        )
    except OSError:
        return ""


def analyze_file(path: Path, root: Path) -> dict:
    """
    Read and analyze a single supported repository file.
    """

    content = read_file_content(path)

    file_info = {
        "path": path.relative_to(root).as_posix(),
        "extension": path.suffix.lower(),
        "language": detect_language(path),
        "size": path.stat().st_size,
        "content": content,
    }

    if file_info["language"] == "Python":
        try:
            file_info["structure"] = extract_python_structure(
                content
            )
        except ValueError:
            file_info["structure"] = {
                "classes": [],
                "functions": [],
                "imports": [],
            }

    return file_info


def scan_repository(repository_path: str) -> list[dict]:
    """
    Scan a repository and return metadata, source content,
    and language-specific analysis for supported files.
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

    files = []

    for path in root.rglob("*"):
        if not path.is_file():
            continue

        if any(
            ignored_directory in path.parts
            for ignored_directory in IGNORED_DIRECTORIES
        ):
            continue

        if not is_supported_file(path):
            continue

        file_size = path.stat().st_size

        if file_size > MAX_FILE_SIZE:
            continue

        files.append(
            analyze_file(
                path,
                root,
            )
        )

    return sorted(
        files,
        key=lambda file: file["path"],
    )