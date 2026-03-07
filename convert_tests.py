#!/usr/bin/env python3
"""
Convert tests/test_plugin.py from test-after-source to TDD mode
"""

import re


def convert_test_plugin():
    filepath = "/Users/zhouzhichao/llm/pytest-inline/tests/test_plugin.py"

    with open(filepath, "r") as f:
        content = f.read()

    # Pattern 1: Simple assignment followed by itest
    # a = a + 1\n            itest().given(a, 1).check_eq(a, 2)
    # ->
    # itest().given(a, 1).check_eq(a, 2)\n            a = a + 1

    # Pattern 2: Multi-line blocks
    # def m(a):\n            a = a + 1\n            itest().given(a, 1).check_eq(a, 2)
    # ->
    # def m(a):\n            itest().given(a, 1).check_eq(a, 2)\n            a = a + 1

    lines = content.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i].rstrip()
        result.append(line)

        # Check if next line is itest() call
        if i + 1 < len(lines):
            next_line = lines[i + 1].rstrip()
            indent1 = len(line) - len(line.lstrip())
            indent2 = len(next_line) - len(next_line.lstrip())

            # Check if we have: statement + itest pattern
            if indent2 > indent1 and "itest()" in next_line or "itest(" in next_line:
                # Check if current line is a source statement (assignment, if, etc.)
                stripped = line.lstrip()
                if (
                    re.match(r"^[a-z_]+\s*=\s*", stripped)
                    or stripped.startswith("if ")
                    or stripped.startswith("elif ")
                    or stripped.startswith("else:")
                    or stripped.startswith("b = ")
                    or stripped.startswith("e = ")
                    or stripped.startswith("match = ")
                ):
                    # Swap them for TDD mode
                    result[-1] = next_line
                    result.append(line)
                    i += 2
                    continue

        i += 1

    # Write back
    with open(filepath, "w") as f:
        f.write("\n".join(result))

    print("Converted tests/test_plugin.py")


if __name__ == "__main__":
    convert_test_plugin()
