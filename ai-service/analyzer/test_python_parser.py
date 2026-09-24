import pytest

from analyzer.python_parser import (
    extract_python_structure,
    parse_python_code,
)


def test_parse_python_code():
    source_code = """
def hello():
    return "Hello DevLens"
"""

    tree = parse_python_code(source_code)

    assert tree is not None


def test_extracts_classes():
    source_code = """
class UserService:
    pass

class RepositoryService:
    pass
"""

    structure = extract_python_structure(source_code)

    assert structure["classes"] == [
        {
            "name": "UserService",
            "line": 2,
        },
        {
            "name": "RepositoryService",
            "line": 5,
        },
    ]


def test_extracts_functions():
    source_code = """
def create_user():
    pass

def delete_user():
    pass
"""

    structure = extract_python_structure(source_code)

    assert structure["functions"] == [
        {
            "name": "create_user",
            "line": 2,
        },
        {
            "name": "delete_user",
            "line": 5,
        },
    ]


def test_extracts_imports():
    source_code = """
import pandas
import requests
from fastapi import FastAPI
from pathlib import Path
"""

    structure = extract_python_structure(source_code)

    assert structure["imports"] == [
        {
            "name": "pandas",
            "line": 2,
        },
        {
            "name": "requests",
            "line": 3,
        },
        {
            "name": "fastapi",
            "line": 4,
        },
        {
            "name": "pathlib",
            "line": 5,
        },
    ]


def test_extracts_complete_structure():
    source_code = """
import pandas
from fastapi import FastAPI

class DataService:

    def load_data(self):
        pass

    def transform_data(self):
        pass
"""

    structure = extract_python_structure(source_code)

    assert structure == {
        "classes": [
            {
                "name": "DataService",
                "line": 5,
            }
        ],
        "functions": [
            {
                "name": "load_data",
                "line": 7,
            },
            {
                "name": "transform_data",
                "line": 10,
            },
        ],
        "imports": [
            {
                "name": "pandas",
                "line": 2,
            },
            {
                "name": "fastapi",
                "line": 3,
            },
        ],
    }


def test_invalid_python_raises_error():
    invalid_source = """
def broken_function(
"""

    with pytest.raises(ValueError):
        parse_python_code(invalid_source)