"""Remove inline_tdd related code from a Python source file.

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


class _ItestddStripper(ast.NodeTransformer):
    """Remove itestdd() expression-statements and inline_tdd imports."""

    def visit_Import(self, node):
        if _is_inline_tdd_import(node):
            return None
        return node

    def visit_ImportFrom(self, node):
        if _is_inline_tdd_import(node):
            return None
        return node

    def visit_Expr(self, node):
        if isinstance(node.value, ast.Call) and _is_itestdd_chain(node.value):
            return None
        return self.generic_visit(node)


def strip_source(source, filename="<string>"):
    """Return *source* with all inline_tdd code removed."""
    tree = ast.parse(source, filename=filename)
    tree = _ItestddStripper().visit(tree)
    ast.fix_missing_locations(tree)
    return ast.unparse(tree)


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="strip-itestdd",
        description="Remove inline_tdd related code from a Python source file.",
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

    if args.inplace:
        with open(args.file, "w", encoding="utf-8") as f:
            f.write(result)
            f.write("\n")
    elif args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
            f.write("\n")
    else:
        sys.stdout.write(result)
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
