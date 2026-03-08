import numpy as np
from inline_tdd import itestdd

# ============================================================
# Basic array creation
# ============================================================

def t_zeros(n):
    itestdd().given(n, 3).check_eq(a.tolist(), [0.0, 0.0, 0.0])
    a = np.zeros(n)
    return a

def t_ones(n):
    itestdd().given(n, 4).check_eq(a.tolist(), [1.0, 1.0, 1.0, 1.0])
    a = np.ones(n)
    return a

def t_arange(n):
    itestdd().given(n, 5).check_eq(a.tolist(), [0, 1, 2, 3, 4])
    a = np.arange(n)
    return a

def t_linspace():
    itestdd().check_eq(a.tolist(), [0.0, 0.5, 1.0])
    a = np.linspace(0, 1, 3)
    return a

def t_full(n):
    itestdd().given(n, 3).check_eq(a.tolist(), [7, 7, 7])
    a = np.full(n, 7)
    return a

def t_eye():
    itestdd().check_eq(a.tolist(), [[1.0, 0.0], [0.0, 1.0]])
    a = np.eye(2)
    return a

# ============================================================
# Arithmetic operations
# ============================================================

def t_add(a, b):
    itestdd().given(a, np.array([1, 2, 3])).given(b, np.array([4, 5, 6])).check_eq(c.tolist(), [5, 7, 9])
    c = a + b
    return c

def t_sub(a, b):
    itestdd().given(a, np.array([10, 20, 30])).given(b, np.array([1, 2, 3])).check_eq(c.tolist(), [9, 18, 27])
    c = a - b
    return c

def t_mul(a, b):
    itestdd().given(a, np.array([2, 3, 4])).given(b, np.array([5, 6, 7])).check_eq(c.tolist(), [10, 18, 28])
    c = a * b
    return c

def t_div(a, b):
    itestdd().given(a, np.array([10.0, 20.0, 30.0])).given(b, np.array([2.0, 4.0, 5.0])).check_eq(c.tolist(), [5.0, 5.0, 6.0])
    c = a / b
    return c

def t_power(a):
    itestdd().given(a, np.array([1, 2, 3])).check_eq(c.tolist(), [1, 4, 9])
    c = a ** 2
    return c

def t_scalar_add(a):
    itestdd().given(a, np.array([1, 2, 3])).check_eq(c.tolist(), [11, 12, 13])
    c = a + 10
    return c

def t_scalar_mul(a):
    itestdd().given(a, np.array([1, 2, 3])).check_eq(c.tolist(), [3, 6, 9])
    c = a * 3
    return c

def t_neg(a):
    itestdd().given(a, np.array([1, -2, 3])).check_eq(c.tolist(), [-1, 2, -3])
    c = -a
    return c

# ============================================================
# Aggregation functions
# ============================================================

def t_sum(a):
    itestdd().given(a, np.array([1, 2, 3, 4])).check_eq(s, 10)
    s = np.sum(a)
    return s

def t_mean(a):
    itestdd().given(a, np.array([2.0, 4.0, 6.0])).check_eq(m, 4.0)
    m = np.mean(a)
    return m

def t_max(a):
    itestdd().given(a, np.array([3, 1, 4, 1, 5])).check_eq(v, 5)
    v = np.max(a)
    return v

def t_min(a):
    itestdd().given(a, np.array([3, 1, 4, 1, 5])).check_eq(v, 1)
    v = np.min(a)
    return v

def t_argmax(a):
    itestdd().given(a, np.array([3, 1, 4, 1, 5])).check_eq(idx, 4)
    idx = np.argmax(a)
    return idx

def t_argmin(a):
    itestdd().given(a, np.array([3, 1, 4, 1, 5])).check_eq(idx, 1)
    idx = np.argmin(a)
    return idx

def t_std(a):
    itestdd().given(a, np.array([2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0])).check_eq(s, 2.0)
    s = np.std(a)
    return s

def t_prod(a):
    itestdd().given(a, np.array([1, 2, 3, 4])).check_eq(p, 24)
    p = np.prod(a)
    return p

def t_cumsum(a):
    itestdd().given(a, np.array([1, 2, 3, 4])).check_eq(c.tolist(), [1, 3, 6, 10])
    c = np.cumsum(a)
    return c

# ============================================================
# Shape manipulation
# ============================================================

def t_reshape(a):
    itestdd().given(a, np.array([1, 2, 3, 4, 5, 6])).check_eq(b.tolist(), [[1, 2, 3], [4, 5, 6]])
    b = a.reshape(2, 3)
    return b

def t_flatten(a):
    itestdd().given(a, np.array([[1, 2], [3, 4]])).check_eq(b.tolist(), [1, 2, 3, 4])
    b = a.flatten()
    return b

def t_transpose(a):
    itestdd().given(a, np.array([[1, 2], [3, 4]])).check_eq(b.tolist(), [[1, 3], [2, 4]])
    b = a.T
    return b

def t_shape(a):
    itestdd().given(a, np.array([[1, 2, 3], [4, 5, 6]])).check_eq(s, (2, 3))
    s = a.shape
    return s

def t_size(a):
    itestdd().given(a, np.array([[1, 2, 3], [4, 5, 6]])).check_eq(n, 6)
    n = a.size
    return n

def t_ndim(a):
    itestdd().given(a, np.array([[1, 2], [3, 4]])).check_eq(d, 2)
    d = a.ndim
    return d

def t_ravel(a):
    itestdd().given(a, np.array([[1, 2], [3, 4]])).check_eq(b.tolist(), [1, 2, 3, 4])
    b = np.ravel(a)
    return b

# ============================================================
# Slicing and indexing
# ============================================================

def t_slice(a):
    itestdd().given(a, np.array([10, 20, 30, 40, 50])).check_eq(b.tolist(), [20, 30, 40])
    b = a[1:4]
    return b

def t_fancy_index(a):
    itestdd().given(a, np.array([10, 20, 30, 40, 50])).check_eq(b.tolist(), [10, 30, 50])
    b = a[[0, 2, 4]]
    return b

def t_bool_index(a):
    itestdd().given(a, np.array([1, 2, 3, 4, 5])).check_eq(b.tolist(), [4, 5])
    b = a[a > 3]
    return b

def t_2d_index(a):
    itestdd().given(a, np.array([[1, 2], [3, 4]])).check_eq(v, 4)
    v = a[1, 1]
    return v

def t_row_slice(a):
    itestdd().given(a, np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])).check_eq(b.tolist(), [4, 5, 6])
    b = a[1, :]
    return b

def t_col_slice(a):
    itestdd().given(a, np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])).check_eq(b.tolist(), [2, 5, 8])
    b = a[:, 1]
    return b

# ============================================================
# Comparison and boolean operations
# ============================================================

def t_gt(a):
    itestdd().given(a, np.array([1, 5, 3, 7, 2])).check_eq(b.tolist(), [False, True, False, True, False])
    b = a > 3
    return b

def t_eq(a):
    itestdd().given(a, np.array([1, 2, 3, 2, 1])).check_eq(b.tolist(), [False, True, False, True, False])
    b = a == 2
    return b

def t_all(a):
    itestdd().given(a, np.array([True, True, True])).check_true(v)
    v = np.all(a)
    return v

def t_any(a):
    itestdd().given(a, np.array([False, False, True])).check_true(v)
    v = np.any(a)
    return v

def t_all_false(a):
    itestdd().given(a, np.array([True, False, True])).check_false(v)
    v = np.all(a)
    return v

# ============================================================
# Sorting and searching
# ============================================================

def t_sort(a):
    itestdd().given(a, np.array([3, 1, 4, 1, 5])).check_eq(b.tolist(), [1, 1, 3, 4, 5])
    b = np.sort(a)
    return b

def t_argsort(a):
    itestdd().given(a, np.array([30, 10, 20])).check_eq(b.tolist(), [1, 2, 0])
    b = np.argsort(a)
    return b

def t_where(a):
    itestdd().given(a, np.array([1, -2, 3, -4])).check_eq(b.tolist(), [1, 0, 3, 0])
    b = np.where(a > 0, a, 0)
    return b

def t_unique(a):
    itestdd().given(a, np.array([3, 1, 2, 1, 3])).check_eq(b.tolist(), [1, 2, 3])
    b = np.unique(a)
    return b

def t_count_nonzero(a):
    itestdd().given(a, np.array([0, 1, 0, 2, 3])).check_eq(n, 3)
    n = np.count_nonzero(a)
    return n

# ============================================================
# Math functions
# ============================================================

def t_abs(a):
    itestdd().given(a, np.array([-1, -2, 3])).check_eq(b.tolist(), [1, 2, 3])
    b = np.abs(a)
    return b

def t_sqrt(a):
    itestdd().given(a, np.array([1.0, 4.0, 9.0])).check_eq(b.tolist(), [1.0, 2.0, 3.0])
    b = np.sqrt(a)
    return b

def t_exp(a):
    itestdd().given(a, np.array([0.0, 1.0])).check_eq(b.tolist(), [1.0, np.e])
    b = np.exp(a)
    return b

def t_log(a):
    itestdd().given(a, np.array([1.0, np.e])).check_eq(b.tolist(), [0.0, 1.0])
    b = np.log(a)
    return b

def t_clip(a):
    itestdd().given(a, np.array([1, 5, 3, 8, 2])).check_eq(b.tolist(), [2, 5, 3, 7, 2])
    b = np.clip(a, 2, 7)
    return b

def t_floor(a):
    itestdd().given(a, np.array([1.7, 2.3, 3.9])).check_eq(b.tolist(), [1.0, 2.0, 3.0])
    b = np.floor(a)
    return b

def t_ceil(a):
    itestdd().given(a, np.array([1.1, 2.5, 3.9])).check_eq(b.tolist(), [2.0, 3.0, 4.0])
    b = np.ceil(a)
    return b

def t_round(a):
    itestdd().given(a, np.array([1.4, 2.5, 3.6])).check_eq(b.tolist(), [1.0, 2.0, 4.0])
    b = np.round(a)
    return b

# ============================================================
# Linear algebra
# ============================================================

def t_dot(a, b):
    itestdd().given(a, np.array([1, 2, 3])).given(b, np.array([4, 5, 6])).check_eq(c, 32)
    c = np.dot(a, b)
    return c

def t_matmul(a, b):
    itestdd().given(a, np.array([[1, 2], [3, 4]])).given(b, np.array([[5, 6], [7, 8]])).check_eq(c.tolist(), [[19, 22], [43, 50]])
    c = np.matmul(a, b)
    return c

def t_det(a):
    itestdd().given(a, np.array([[1.0, 2.0], [3.0, 4.0]])).check_eq(round(d, 10), -2.0)
    d = np.linalg.det(a)
    return d

def t_inv(a):
    itestdd().given(a, np.array([[1.0, 2.0], [3.0, 4.0]])).check_eq(b.tolist(), [[-2.0, 1.0], [1.5, -0.5]])
    b = np.round(np.linalg.inv(a), 10)
    return b

def t_norm(a):
    itestdd().given(a, np.array([3.0, 4.0])).check_eq(n, 5.0)
    n = np.linalg.norm(a)
    return n

# ============================================================
# Concatenation and stacking
# ============================================================

def t_concat(a, b):
    itestdd().given(a, np.array([1, 2])).given(b, np.array([3, 4])).check_eq(c.tolist(), [1, 2, 3, 4])
    c = np.concatenate([a, b])
    return c

def t_vstack(a, b):
    itestdd().given(a, np.array([1, 2])).given(b, np.array([3, 4])).check_eq(c.tolist(), [[1, 2], [3, 4]])
    c = np.vstack([a, b])
    return c

def t_hstack(a, b):
    itestdd().given(a, np.array([[1], [2]])).given(b, np.array([[3], [4]])).check_eq(c.tolist(), [[1, 3], [2, 4]])
    c = np.hstack([a, b])
    return c

def t_split(a):
    itestdd().given(a, np.array([1, 2, 3, 4, 5, 6])).check_eq(len(parts), 3)
    parts = np.split(a, 3)
    return parts

# ============================================================
# Type conversion
# ============================================================

def t_astype_float(a):
    itestdd().given(a, np.array([1, 2, 3])).check_eq(b.tolist(), [1.0, 2.0, 3.0])
    b = a.astype(float)
    return b

def t_astype_int(a):
    itestdd().given(a, np.array([1.9, 2.1, 3.7])).check_eq(b.tolist(), [1, 2, 3])
    b = a.astype(int)
    return b

def t_dtype(a):
    itestdd().given(a, np.array([1, 2, 3])).check_eq(d, np.dtype("int64"))
    d = a.dtype
    return d

# ============================================================
# Parameterized tests
# ============================================================

def t_param_add(a):
    itestdd(parameterized=True).given(a, [np.array([1, 2]), np.array([10, 20])]).check_eq(b.tolist(), [[2, 3], [11, 21]])
    b = a + 1
    return b

# ============================================================
# Multiple tests on same statement
# ============================================================

def t_multi(a):
    itestdd().given(a, np.array([1, 2, 3])).check_eq(b.tolist(), [2, 4, 6])
    itestdd().given(a, np.array([0, 0, 0])).check_eq(b.tolist(), [0, 0, 0])
    itestdd().given(a, np.array([-1, -2, -3])).check_eq(b.tolist(), [-2, -4, -6])
    b = a * 2
    return b

# ============================================================
# Edge cases
# ============================================================

def t_empty(a):
    itestdd().given(a, np.array([])).check_eq(s, 0.0)
    s = np.sum(a)
    return s

def t_single(a):
    itestdd().given(a, np.array([42])).check_eq(m, 42.0)
    m = np.mean(a)
    return m

def t_nan_check(a):
    itestdd().given(a, np.array([1.0, np.nan, 3.0])).check_eq(n, 1)
    n = np.count_nonzero(np.isnan(a))
    return n

def t_inf(a):
    itestdd().given(a, np.array([1.0, np.inf, -np.inf])).check_eq(n, 2)
    n = np.count_nonzero(np.isinf(a))
    return n

def t_bool_array(a):
    itestdd().given(a, np.array([True, False, True, True])).check_eq(n, 3)
    n = np.sum(a)
    return n
