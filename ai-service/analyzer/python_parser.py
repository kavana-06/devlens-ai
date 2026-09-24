import ast


def parse_python_code(source_code: str) -> ast.AST:
    """
    Parse Python source code into an Abstract Syntax Tree.
    """

    try:
        return ast.parse(source_code)
    except SyntaxError as exception:
        raise ValueError(
            f"Unable to parse Python source code: {exception}"
        ) from exception


def extract_python_structure(source_code: str) -> dict:
    """
    Extract structural information from Python source code.
    """

    tree = parse_python_code(source_code)

    classes = []
    functions = []
    imports = []

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            classes.append(
                {
                    "name": node.name,
                    "line": node.lineno,
                }
            )

        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions.append(
                {
                    "name": node.name,
                    "line": node.lineno,
                }
            )

        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(
                    {
                        "name": alias.name,
                        "line": node.lineno,
                    }
                )

        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(
                    {
                        "name": node.module,
                        "line": node.lineno,
                    }
                )

    return {
        "classes": classes,
        "functions": functions,
        "imports": imports,
    }