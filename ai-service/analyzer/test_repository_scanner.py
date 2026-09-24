from pathlib import Path

from analyzer.repository_scanner import scan_repository


def test_scan_repository(tmp_path: Path):
    backend_directory = tmp_path / "backend"
    backend_directory.mkdir()

    app_file = backend_directory / "app.py"
    app_file.write_text("print('hello')")

    readme_file = tmp_path / "README.md"
    readme_file.write_text("# Test Repository")

    image_file = tmp_path / "image.png"
    image_file.write_bytes(b"fake image data")

    git_directory = tmp_path / ".git"
    git_directory.mkdir()
    (git_directory / "config").write_text("ignored")

    node_modules_directory = tmp_path / "node_modules"
    node_modules_directory.mkdir()
    (node_modules_directory / "package.js").write_text("ignored")

    files = scan_repository(str(tmp_path))

    file_paths = [file["path"] for file in files]

    assert "backend/app.py" in file_paths
    assert "README.md" in file_paths
    assert "image.png" not in file_paths
    assert ".git/config" not in file_paths
    assert "node_modules/package.js" not in file_paths


def test_detects_file_metadata(tmp_path: Path):
    app_file = tmp_path / "app.py"
    app_file.write_text("print('hello')")

    files = scan_repository(str(tmp_path))

    assert len(files) == 1

    file_info = files[0]

    assert file_info["path"] == "app.py"
    assert file_info["extension"] == ".py"
    assert file_info["language"] == "Python"
    assert file_info["size"] > 0


def test_reads_file_content(tmp_path: Path):
    app_file = tmp_path / "app.py"

    source_code = "def hello():\n    return 'Hello DevLens'"

    app_file.write_text(source_code)

    files = scan_repository(str(tmp_path))

    assert len(files) == 1
    assert files[0]["content"] == source_code


def test_skips_large_files(tmp_path: Path):
    large_file = tmp_path / "large.py"

    large_file.write_text("x" * 1_000_001)

    files = scan_repository(str(tmp_path))

    assert files == []