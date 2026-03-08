"""Comment out inline_tdd related code from a Python source file.

Usage:
    strip-itestdd <file>              # print cleaned code to stdout
    strip-itestdd <file> -i           # edit the file in-place
    strip-itestdd <file> -o out.py    # write to a different file
"""

import argparse
import ast
import sys


def _is_itestdd_chain(node):
    """Return True if *node* is an itestdd() call or a method chain on one."""
    if isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name) and node.func.id == "itestdd":
            return True
        if isinstance(node.func, ast.Attribute) and isinstance(
            node.func.value, ast.Call
        ):
            return _is_itestdd_chain(node.func.value)
    return False


def _is_inline_tdd_import(node):
    """Return True if *node* is an import statement that imports inline_tdd."""
    if isinstance(node, ast.Import):
        return any(alias.name.split(".")[0] == "inline_tdd" for alias in node.names)
    if isinstance(node, ast.ImportFrom):
        return node.module is not None and node.module.split(".")[0] == "inline_tdd"
    return False


def _collect_lines_to_comment(tree):
    """Walk the AST and return a set of 1-based line numbers to comment out."""
    lines = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)) and _is_inline_tdd_import(node):
            end = getattr(node, "end_lineno", None) or node.lineno
            for ln in range(node.lineno, end + 1):
                lines.add(ln)
        elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Call) and _is_itestdd_chain(node.value):
            end = getattr(node, "end_lineno", None) or node.lineno
            for ln in range(node.lineno, end + 1):
                lines.add(ln)
    return lines


def strip_source(source, filename="<string>"):
    """Return *source* with all inline_tdd code commented out."""
    tree = ast.parse(source, filename=filename)
    lines_to_comment = _collect_lines_to_comment(tree)
    if not lines_to_comment:
        return source

    result = []
    for i, line in enumerate(source.splitlines(keepends=True), start=1):
        if i in lines_to_comment:
            # Preserve indentation: find leading whitespace, then prepend "# "
            stripped = line.rstrip("\n\r")
            indent = len(stripped) - len(stripped.lstrip())
            commented = stripped[:indent] + "# " + stripped[indent:]
            # Preserve original line ending
            ending = line[len(stripped):]
            result.append(commented + ending)
        else:
            result.append(line)
    return "".join(result)


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="strip-itestdd",
        description="Comment out inline_tdd related code in a Python source file.",
    )
    parser.add_argument("file", help="Python source file to process")
    parser.add_argument(
        "-i", "--inplace", action="store_true", help="edit the file in-place"
    )
    parser.add_argument("-o", "--output", help="write output to this file")
    args = parser.parse_args(argv)

    with open(args.file, "r", encoding="utf-8") as f:
        source = f.read()

    result = strip_source(source, filename=args.file)

    # Ensure file ends with newline
    if not result.endswith("\n"):
        result += "\n"

    if args.inplace:
        with open(args.file, "w", encoding="utf-8") as f:
            f.write(result)
    elif args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
    else:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()
