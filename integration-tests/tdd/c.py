from inline_tdd import itestdd

# ============================================================
# parameterized=True: basic cases
# ============================================================

def param_add(a):
    itestdd(parameterized=True).given(a, [1, 2, 3, 4, 5]).check_eq(b, [2, 4, 6, 8, 10])
    b = a * 2

def param_sub(a, c):
    itestdd(parameterized=True).given(a, [10, 20, 30]).given(c, [1, 2, 3]).check_eq(b, [9, 18, 27])
    b = a - c

def param_string(s):
    itestdd(parameterized=True).given(s, ["hello", "world", ""]).check_eq(r, [5, 5, 0])
    r = len(s)

def param_bool(x):
    itestdd(parameterized=True).given(x, [0, 1, -1, "", "a"]).check_eq(b, [False, True, True, False, True])
    b = bool(x)

# ============================================================
# parameterized + check_true / check_false
# ============================================================

def param_check_eq_true(a):
    itestdd(parameterized=True).given(a, [2, 4, 6, 100]).check_eq(b, [True, True, True, True])
    b = a % 2 == 0

def param_check_eq_false(a):
    itestdd(parameterized=True).given(a, [2, 4, 6, 100]).check_eq(b, [False, False, False, False])
    b = a % 2 == 1

# ============================================================
# parameterized + check_neq
# ============================================================

def param_neq(a):
    itestdd(parameterized=True).given(a, [1, 2, 3]).check_neq(b, [0, 0, 0])
    b = a + 1

# ============================================================
# parameterized + check_none / check_not_none
# ============================================================

def param_is_none(a):
    itestdd(parameterized=True).given(a, [None, None, None]).check_eq(b, [None, None, None])
    b = a

def param_is_not_none(a):
    itestdd(parameterized=True).given(a, [1, "x", True]).check_neq(b, [None, None, None])
    b = a

# ============================================================
# parameterized + test_name
# ============================================================

def param_named(a):
    itestdd(test_name="square-params", parameterized=True).given(a, [1, 2, 3, 4]).check_eq(b, [1, 4, 9, 16])
    b = a ** 2

# ============================================================
# parameterized + tag
# ============================================================

def param_tagged(a):
    itestdd(parameterized=True, tag=["math"]).given(a, [0, 1, 2]).check_eq(b, [0, 1, 4])
    b = a ** 2

# ============================================================
# parameterized + repeated
# ============================================================

def param_repeated(a):
    itestdd(parameterized=True, repeated=2).given(a, [10, 20]).check_eq(b, [11, 21])
    b = a + 1

# ============================================================
# parameterized with multiple givens
# ============================================================

def param_multi_given(a, b):
    itestdd(parameterized=True).given(a, [1, 2, 3]).given(b, [10, 20, 30]).check_eq(c, [11, 22, 33])
    c = a + b

def param_three_givens(a, b, c):
    itestdd(parameterized=True).given(a, [1, 2]).given(b, [3, 4]).given(c, [5, 6]).check_eq(r, [9, 12])
    r = a + b + c

# ============================================================
# parameterized with different data types
# ============================================================

def param_floats(a):
    itestdd(parameterized=True).given(a, [1.5, 2.5, 3.0]).check_eq(b, [3.0, 5.0, 6.0])
    b = a * 2

def param_negative(a):
    itestdd(parameterized=True).given(a, [-1, -5, -10]).check_eq(b, [1, 5, 10])
    b = abs(a)

def param_lists(a):
    itestdd(parameterized=True).given(a, [[1, 2], [3, 4], [5]]).check_eq(b, [2, 2, 1])
    b = len(a)

# ============================================================
# parameterized edge cases
# ============================================================

def param_single(a):
    """Parameterized with single element lists"""
    itestdd(parameterized=True).given(a, [42]).check_eq(b, [43])
    b = a + 1

def param_zeros(a):
    itestdd(parameterized=True).given(a, [0, 0, 0]).check_eq(b, [0, 0, 0])
    b = a * 0

# ============================================================
# repeated (non-parameterized)
# ============================================================

def repeated_basic(a):
    itestdd(repeated=5).given(a, 3).check_eq(b, 9)
    b = a ** 2

def repeated_with_name(a):
    itestdd(test_name="rep-named", repeated=3).given(a, 2).check_eq(b, 4)
    b = a * 2

def repeated_with_tag(a):
    itestdd(repeated=2, tag=["stable"]).given(a, 10).check_eq(b, 100)
    b = a * 10

# ============================================================
# tag filtering
# ============================================================

def tagged_single(a):
    itestdd(tag=["fast"]).given(a, 1).check_eq(b, 2)
    b = a + 1

def tagged_multi(a):
    itestdd(tag=["fast", "math"]).given(a, 5).check_eq(b, 25)
    b = a ** 2

# ============================================================
# test_name
# ============================================================

def named_simple(a):
    itestdd(test_name="my-test").given(a, 7).check_eq(b, 14)
    b = a * 2

def named_descriptive(a):
    itestdd(test_name="absolute-value-of-negative").given(a, -42).check_eq(b, 42)
    b = abs(a)

# ============================================================
# timeout
# ============================================================

def with_timeout(a):
    itestdd(timeout=5.0).given(a, 3).check_eq(b, 6)
    b = a + a

def timeout_with_params(a):
    itestdd(parameterized=True, timeout=5.0).given(a, [1, 2, 3]).check_eq(b, [2, 4, 6])
    b = a * 2

# ============================================================
# combining multiple parameters
# ============================================================

def all_params_combined(a):
    itestdd(test_name="combo", parameterized=True, repeated=2, tag=["combo"], timeout=5.0).given(a, [1, 2]).check_eq(b, [3, 4])
    b = a + 2

def name_and_tag(a):
    itestdd(test_name="labeled", tag=["unit"]).given(a, 10).check_eq(b, 5)
    b = a // 2

def name_tag_repeated(a):
    itestdd(test_name="triple-check", repeated=3, tag=["core"]).given(a, 4).check_eq(b, 16)
    b = a * 4

T = 12 * 4
def calculate_with_T(a):
    itestdd().given(a, 3).check_eq(b, 51)
    b = T + a