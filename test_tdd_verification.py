#!/usr/bin/env python3
"""
Test to verify TDD mode works correctly
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

import ast
from inline.plugin import ExtractInlineTest


def test_tdd_mode():
    """Test that TDD mode works: test before source"""

    # Test case 1: Simple function
    code1 = """
from inline import itest

def add(a, b):
    itest().given(a, 2).given(b, 3).check_eq(result, 5)
    result = a + b
    return result
"""

    tree = ast.parse(code1)
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            child.parent = node
            if isinstance(child, ast.stmt):
                node.children = [child] + getattr(node, "children", [])

    extractor = ExtractInlineTest()
    extractor.inline_module_imported = True
    extractor.visit(tree)

    assert len(extractor.inline_test_list) == 1, f"Expected 1 test, got {len(extractor.inline_test_list)}"
    test = extractor.inline_test_list[0]

    # Verify the test is testing the correct statement
    from inline.plugin import ExtractInlineTest as ET

    source_code = ET.node_to_source_code(test.previous_stmts[0])
    assert "result = a + b" in source_code, f"Expected to test assignment, got: {source_code}"

    print("✓ Test 1 passed: TDD mode works for function")

    # Test case 2: Module level
    code2 = """
from inline import itest

x = 0
itest().given(x, 5).check_eq(x, 5)
x = x + 1
"""

    tree = ast.parse(code2)
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            child.parent = node
            if isinstance(child, ast.stmt):
                node.children = [child] + getattr(node, "children", [])

    extractor = ExtractInlineTest()
    extractor.inline_module_imported = True
    extractor.visit(tree)

    assert len(extractor.inline_test_list) == 1, f"Expected 1 test, got {len(extractor.inline_test_list)}"
    test = extractor.inline_test_list[0]

    source_code = ET.node_to_source_code(test.previous_stmts[0])
    assert "x = x + 1" in source_code, f"Expected to test increment, got: {source_code}"

    print("✓ Test 2 passed: TDD mode works for module level")

    print("\n=== All TDD mode verification tests passed! ===")


if __name__ == "__main__":
    test_tdd_mode()
