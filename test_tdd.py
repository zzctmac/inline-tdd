#!/usr/bin/env python3
"""
Quick test to verify TDD mode works
"""

import ast
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from inline.plugin import ExtractInlineTest

test_code = """
from inline import itest

def m(a):
    itest().given(a, 1).check_eq(a, 2)
    a = a + 1
"""

try:
    tree = ast.parse(test_code)

    # Bind parent and children
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            child.parent = node
            if isinstance(child, ast.stmt):
                node.children = [child] if not hasattr(node, "children") else [child] + node.children

    extractor = ExtractInlineTest()
    extractor.inline_module_imported = True
    extractor.visit(tree)

    print(f"Found {len(extractor.inline_test_list)} inline tests")
    if extractor.inline_test_list:
        test = extractor.inline_test_list[0]
        print(f"Test name: {test.test_name}")
        print(f"Line number: {test.lineno}")
        print(f"Previous statements: {len(test.previous_stmts)}")
        if test.previous_stmts:
            from inline.plugin import ExtractInlineTest as ET

            print(f"Source code: {ET.node_to_source_code(test.previous_stmts[0])}")
        print("TDD mode appears to work!")
    else:
        print("No inline tests found - TDD mode may not be working")

except Exception as e:
    print(f"Error: {e}")
    import traceback

    traceback.print_exc()
