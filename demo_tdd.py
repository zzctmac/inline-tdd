#!/usr/bin/env python3
"""
Demo: TDD mode in action
"""

print("=" * 60)
print("pytest-inline TDD 模式演示")
print("=" * 60)
print()
print("在 TDD 模式下，测试写在源代码之前：")
print()
print("示例 1: 函数测试")
print("-" * 60)
print("""
def add(a, b):
    # 先写测试 (TDD风格)
    itest().given(a, 2).given(b, 3).check_eq(result, 5)
    # 再写实现
    result = a + b
    return result
""")
print()
print("示例 2: 模块级别测试")
print("-" * 60)
print("""
from inline import itest

x = 0
# 先写测试
itest().given(x, 5).check_eq(x, 5)
# 再写实现
x = x + 1
""")
print()
print("=" * 60)
print("核心实现：find_following_stmt()")
print("=" * 60)
print("现在 inline test 会选择它后面的源代码行进行测试")
print()
print("相关代码文件：")
print("  - src/inline/plugin.py:344 (find_following_stmt)")
print("  - src/inline/plugin.py:1057 (visit_Expr)")
print()
print("运行验证: python test_tdd_verification.py")
print("运行测试: python -m pytest tests/test_plugin.py -q")
