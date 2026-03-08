"""Comment out inline_tdd related code from a Python source file.

Usage:
    strip-itestdd <file>              # print cleaned code to stdout
    strip-itestdd <file> -i           # edit the file in-place
    strip-itestdd <file> -o out.py    # write to a different file
"""

import argparse
import ast
import io
import sys
import tokenize


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


def _statement_end_lineno(tokens, start_lineno):
    """Find the end line of the statement that starts at *start_lineno*."""
    started = False
    depth = 0
    candidate = start_lineno

    for tok in tokens:
        tok_type, tok_str, (srow, _), (erow, _), _ = tok
        if erow < start_lineno:
            continue

        if not started:
            if srow < start_lineno:
                continue
            if tok_type in {
                tokenize.NL,
                tokenize.NEWLINE,
                tokenize.INDENT,
                tokenize.DEDENT,
                tokenize.COMMENT,
                tokenize.ENCODING,
            }:
                continue
            started = True

        if tok_type == tokenize.OP:
            if tok_str in "([{":
                depth += 1
            elif tok_str in ")]}" and depth > 0:
                depth -= 1

        candidate = max(candidate, erow)
        if tok_type == tokenize.NEWLINE and depth == 0:
            return erow

    return candidate


def _collect_lines_to_comment(tree, source):
    """Walk the AST and return a set of 1-based line numbers to comment out."""
    tokens = list(tokenize.generate_tokens(io.StringIO(source).readline))
    lines = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)) and _is_inline_tdd_import(node):
            end = getattr(node, "end_lineno", None) or _statement_end_lineno(
                tokens, node.lineno
            )
            for ln in range(node.lineno, end + 1):
                lines.add(ln)
        elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Call) and _is_itestdd_chain(node.value):
            end = getattr(node, "end_lineno", None) or _statement_end_lineno(
                tokens, node.lineno
            )
            for ln in range(node.lineno, end + 1):
                lines.add(ln)
    return lines


def strip_source(source, filename="<string>"):
    """Return *source* with all inline_tdd code commented out."""
    tree = ast.parse(source, filename=filename)
    lines_to_comment = _collect_lines_to_comment(tree, source)
    if not lines_to_comment:
        return source

    result = []
    for i, line in enumerate(source.splitlines(keepends=True), start=1):
        if i in lines_to_comment:
            stripped = line.rstrip("\n\r")
            if not stripped.strip():
                # Keep blank lines untouched to avoid introducing visual noise.
                result.append(line)
                continue
            indent = len(stripped) - len(stripped.lstrip())
            if stripped[indent:].startswith("#"):
                # Idempotent: do not re-comment lines that are already comments.
                result.append(line)
                continue
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
