#!/usr/bin/env python3
"""
Convert test files from test-after-source to TDD mode (test-before-source)
"""

import re
import sys
from pathlib import Path


def convert_file(filepath):
    """Convert a single file to TDD mode"""
    with open(filepath, "r") as f:
        content = f.read()

    lines = content.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # Skip imports and initial variable declarations
        if (
            line.startswith("from inline_tdd import")
            or line.startswith("import ")
            or re.match(r"^[a-z] = (0|1)$", line)
            or line.startswith("sleep =")
        ):
            result.append(lines[i])
            i += 1
            continue

        # Find source statements followed by tests
        if re.match(r"^[a-z] = [a-z] (\+|\-|\*|/) \d+$", line):
            # Collect all following test statements
            test_lines = []
            j = i + 1
            while j < len(lines) and lines[j].strip().startswith("itestdd("):
                test_lines.append(lines[j])
                j += 1

            # Add tests first, then source (TDD mode)
            if test_lines:
                result.extend(test_lines)
                result.append(lines[i])
            else:
                # No tests following, keep as is
                result.append(lines[i])

            i = j
        else:
            result.append(lines[i])
            i += 1

    # Write back
    with open(filepath, "w") as f:
        f.write("\n".join(result))

    print(f"Converted {filepath}")


def main():
    test_dir = Path("/Users/zhouzhichao/llm/pytest-inline/integration-tests/parallelization/test_files")

    for filepath in test_dir.glob("*.py"):
        convert_file(filepath)

    print("All files converted successfully!")


if __name__ == "__main__":
    main()
