from inline_tdd import itestdd
import math

# ============================================================
# Existing tests
# ============================================================

def t(a):
    itestdd().given(a, 1).check_eq(b, 2)
    b = a + 1
    return b

def t2(a):
    itestdd().given(a, 10).check_eq(b, 9)
    itestdd().given(a, 1).check_eq(b, 2)
    if a < 10:
        itestdd().given(a, 1).check_eq(b, 2)
        b = a + 1
    else:
        b = a - 1
    return b

def t3(a):
    b = 0
    itestdd().given(a, 3).check_eq(b, 6)
    itestdd().given(a, 0).check_eq(b, 0)
    itestdd().given(a, 1).check_eq(b, 2)
    for _ in range(a):
        itestdd().given(b, 3).check_eq(b, 5)
        b += 2
    return b

# ============================================================
# Arithmetic operations
# ============================================================

def t_sub(a):
    itestdd().given(a, 5).check_eq(b, 3)
    b = a - 2
    return b

def t_mul(a):
    itestdd().given(a, 3).check_eq(b, 9)
    b = a * 3
    return b

def t_div(a):
    itestdd().given(a, 10).check_eq(b, 5.0)
    b = a / 2
    return b

def t_floordiv(a):
    itestdd().given(a, 7).check_eq(b, 3)
    b = a // 2
    return b

def t_mod(a):
    itestdd().given(a, 7).check_eq(b, 1)
    b = a % 2
    return b

def t_pow(a):
    itestdd().given(a, 3).check_eq(b, 9)
    b = a ** 2
    return b

def t_neg(a):
    itestdd().given(a, 5).check_eq(b, -5)
    b = -a
    return b

def t_complex_expr(a):
    itestdd().given(a, 2).check_eq(b, 7)
    b = a * 3 + 1
    return b

# ============================================================
# Different check types
# ============================================================

def t_check_neq(a):
    itestdd().given(a, 1).check_neq(b, 1)
    b = a + 1
    return b

def t_check_true(a):
    itestdd().given(a, 5).check_true(b > 3)
    b = a + 1
    return b

def t_check_false(a):
    itestdd().given(a, 1).check_false(b > 5)
    b = a + 1
    return b

def t_check_none(a):
    itestdd().given(a, None).check_none(b)
    b = a
    return b

def t_check_not_none(a):
    itestdd().given(a, 42).check_not_none(b)
    b = a
    return b

def t_check_same():
    x = [1, 2, 3]
    itestdd().check_same(y, x)
    y = x
    return y

def t_check_not_same():
    x = [1, 2, 3]
    itestdd().check_not_same(y, x)
    y = list(x)
    return y

# ============================================================
# Multiple givens
# ============================================================

def t_multi_given(a, c):
    itestdd().given(a, 2).given(c, 3).check_eq(b, 5)
    b = a + c
    return b

def t_three_givens(a, b, c):
    itestdd().given(a, 1).given(b, 2).given(c, 3).check_eq(d, 6)
    d = a + b + c
    return d

# ============================================================
# Named / tagged / repeated tests
# ============================================================

def t_named(a):
    itestdd(test_name="custom-addition").given(a, 10).check_eq(b, 11)
    b = a + 1
    return b

def t_tagged(a):
    itestdd(test_name="tagged-test", tag=["math"]).given(a, 1).check_eq(b, 2)
    b = a + 1
    return b

def t_repeated(a):
    itestdd(repeated=3).given(a, 1).check_eq(b, 2)
    b = a + 1
    return b

# ============================================================
# Parameterized tests
# ============================================================

def t_parameterized(a):
    itestdd(parameterized=True).given(a, [1, 2, 3]).check_eq(b, [2, 3, 4])
    b = a + 1
    return b

def t_parameterized_mul(a):
    itestdd(parameterized=True).given(a, [0, 1, 5, -2]).check_eq(b, [0, 2, 10, -4])
    b = a * 2
    return b

# ============================================================
# Assume (conditional test execution)
# ============================================================

def t_assume_true(a):
    itestdd().assume(True).given(a, 1).check_eq(b, 2)
    b = a + 1
    return b

def t_assume_false(a):
    itestdd().assume(False).given(a, 1).check_eq(b, 999)
    b = a + 1
    return b

# ============================================================
# String operations
# ============================================================

def t_str_concat(a):
    itestdd().given(a, "hello").check_eq(b, "hello world")
    b = a + " world"
    return b

def t_str_repeat(a):
    itestdd().given(a, "ab").check_eq(b, "ababab")
    b = a * 3
    return b

def t_str_upper(a):
    itestdd().given(a, "hello").check_eq(b, "HELLO")
    b = a.upper()
    return b

def t_str_len(a):
    itestdd().given(a, "hello").check_eq(b, 5)
    b = len(a)
    return b

def t_str_strip(a):
    itestdd().given(a, "  hello  ").check_eq(b, "hello")
    b = a.strip()
    return b

def t_str_replace(a):
    itestdd().given(a, "hello world").check_eq(b, "hello python")
    b = a.replace("world", "python")
    return b

# ============================================================
# List operations
# ============================================================

def t_list_concat(a):
    itestdd().given(a, [1, 2]).check_eq(b, [1, 2, 3])
    b = a + [3]
    return b

def t_list_len(a):
    itestdd().given(a, [1, 2, 3]).check_eq(b, 3)
    b = len(a)
    return b

def t_list_sum(a):
    itestdd().given(a, [1, 2, 3, 4]).check_eq(b, 10)
    b = sum(a)
    return b

def t_list_sorted(a):
    itestdd().given(a, [3, 1, 2]).check_eq(b, [1, 2, 3])
    b = sorted(a)
    return b

def t_list_reversed(a):
    itestdd().given(a, [1, 2, 3]).check_eq(b, [3, 2, 1])
    b = list(reversed(a))
    return b

def t_list_slice(a):
    itestdd().given(a, [1, 2, 3, 4, 5]).check_eq(b, [2, 3, 4])
    b = a[1:4]
    return b

def t_list_comp(a):
    itestdd().given(a, [1, 2, 3]).check_eq(b, [2, 4, 6])
    b = [x * 2 for x in a]
    return b

# ============================================================
# Dict operations
# ============================================================

def t_dict_create(a):
    itestdd().given(a, "key").check_eq(b, {"key": 1})
    b = {a: 1}
    return b

def t_dict_len(a):
    itestdd().given(a, {"x": 1, "y": 2}).check_eq(b, 2)
    b = len(a)
    return b

# ============================================================
# Tuple operations
# ============================================================

def t_tuple_create(a, c):
    itestdd().given(a, 1).given(c, 2).check_eq(b, (1, 2))
    b = (a, c)
    return b

def t_tuple_len(a):
    itestdd().given(a, (1, 2, 3)).check_eq(b, 3)
    b = len(a)
    return b

# ============================================================
# Set operations
# ============================================================

def t_set_create(a):
    itestdd().given(a, [1, 2, 2, 3]).check_eq(b, {1, 2, 3})
    b = set(a)
    return b

# ============================================================
# Boolean operations
# ============================================================

def t_bool_and(a):
    itestdd().given(a, 5).check_true(b)
    b = a > 0 and a < 10
    return b

def t_bool_and_false(a):
    itestdd().given(a, 15).check_false(b)
    b = a > 0 and a < 10
    return b

def t_bool_or(a):
    itestdd().given(a, -1).check_true(b)
    b = a > 0 or a < 0
    return b

def t_bool_not(a):
    itestdd().given(a, True).check_false(b)
    b = not a
    return b

# ============================================================
# Multiple tests on same statement
# ============================================================

def t_multi_test(a):
    itestdd().given(a, 1).check_eq(b, 2)
    itestdd().given(a, 0).check_eq(b, 1)
    itestdd().given(a, -1).check_eq(b, 0)
    itestdd().given(a, 100).check_eq(b, 101)
    b = a + 1
    return b

# ============================================================
# Conditional expression (ternary)
# ============================================================

def t_ternary(a):
    itestdd().given(a, 5).check_eq(b, "positive")
    itestdd().given(a, -1).check_eq(b, "non-positive")
    b = "positive" if a > 0 else "non-positive"
    return b

# ============================================================
# Nested if/elif/else
# ============================================================

def t_elif(a):
    itestdd().given(a, 15).check_eq(b, "large")
    itestdd().given(a, 5).check_eq(b, "medium")
    itestdd().given(a, -1).check_eq(b, "small")
    if a > 10:
        b = "large"
    elif a > 0:
        b = "medium"
    else:
        b = "small"
    return b

# ============================================================
# While loop
# ============================================================

def t_while(a):
    b = 0
    itestdd().given(a, 3).check_eq(b, 3)
    while a > 0:
        b += 1
        a -= 1
    return b

# ============================================================
# Built-in functions
# ============================================================

def t_abs(a):
    itestdd().given(a, -3).check_eq(b, 3)
    b = abs(a)
    return b

def t_max(a, c):
    itestdd().given(a, 3).given(c, 5).check_eq(b, 5)
    b = max(a, c)
    return b

def t_min(a, c):
    itestdd().given(a, 3).given(c, 5).check_eq(b, 3)
    b = min(a, c)
    return b

def t_round(a):
    itestdd().given(a, 3.7).check_eq(b, 4)
    b = round(a)
    return b

def t_int_cast(a):
    itestdd().given(a, "42").check_eq(b, 42)
    b = int(a)
    return b

def t_str_cast(a):
    itestdd().given(a, 42).check_eq(b, "42")
    b = str(a)
    return b

def t_float_cast(a):
    itestdd().given(a, "3.14").check_eq(b, 3.14)
    b = float(a)
    return b

def t_math_sqrt(a):
    itestdd().given(a, 4).check_eq(b, 2.0)
    b = math.sqrt(a)
    return b

# ============================================================
# Augmented assignment
# ============================================================

def t_aug_add(a):
    itestdd().given(a, 5).check_eq(a, 8)
    a += 3
    return a

def t_aug_sub(a):
    itestdd().given(a, 5).check_eq(a, 2)
    a -= 3
    return a

def t_aug_mul(a):
    itestdd().given(a, 5).check_eq(a, 15)
    a *= 3
    return a

# ============================================================
# Multiple preceding statements used by target
# ============================================================

def t_multi_stmt(a):
    c = 10
    d = 20
    itestdd().given(a, 5).check_eq(b, 35)
    b = a + c + d
    return b

def t_multi_stmt2(a):
    x = 2
    y = 3
    z = 4
    itestdd().given(a, 1).check_eq(b, 10)
    b = a + x + y + z
    return b

# ============================================================
# Chained comparison
# ============================================================

def t_chained_cmp(a):
    itestdd().given(a, 5).check_true(b)
    itestdd().given(a, 15).check_false(b)
    b = 0 < a < 10
    return b

# ============================================================
# Edge cases
# ============================================================

def t_zero(a):
    itestdd().given(a, 0).check_eq(b, 0)
    b = a * 100
    return b

def t_empty_str(a):
    itestdd().given(a, "").check_eq(b, 0)
    b = len(a)
    return b

def t_empty_list(a):
    itestdd().given(a, []).check_eq(b, 0)
    b = len(a)
    return b

def t_negative(a):
    itestdd().given(a, -10).check_eq(b, -7)
    b = a + 3
    return b

def t_large_number(a):
    itestdd().given(a, 1000000).check_eq(b, 1000001)
    b = a + 1
    return b

def t_float_arith(a):
    itestdd().given(a, 0.1).check_eq(b, 0.30000000000000004)
    b = a + 0.2
    return b

def t_bool_to_int(a):
    itestdd().given(a, True).check_eq(b, 1)
    b = int(a)
    return b

# ============================================================
# For loop with inner test on statement
# ============================================================

def t_for_inner(a):
    b = 0
    itestdd().given(a, 5).check_eq(b, 50)
    for _ in range(a):
        itestdd().given(b, 0).check_eq(b, 10)
        b += 10
    return b

# ============================================================
# Nested control flow: if inside for
# ============================================================

def t_for_if(a):
    b = 0
    itestdd().given(a, 6).check_eq(b, 3)
    itestdd().given(a, 0).check_eq(b, 0)
    for i in range(a):
        if i % 2 == 0:
            b += 1
    return b
