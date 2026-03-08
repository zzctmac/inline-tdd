import math

def t(a):
    b = a + 1
    return b

def t2(a):
    if a < 10:
        b = a + 1
    else:
        b = a - 1
    return b

def t3(a):
    b = 0
    for _ in range(a):
        b += 2
    return b

def t_sub(a):
    b = a - 2
    return b

def t_mul(a):
    b = a * 3
    return b

def t_div(a):
    b = a / 2
    return b

def t_floordiv(a):
    b = a // 2
    return b

def t_mod(a):
    b = a % 2
    return b

def t_pow(a):
    b = a ** 2
    return b

def t_neg(a):
    b = -a
    return b

def t_complex_expr(a):
    b = a * 3 + 1
    return b

def t_check_neq(a):
    b = a + 1
    return b

def t_check_true(a):
    b = a + 1
    return b

def t_check_false(a):
    b = a + 1
    return b

def t_check_none(a):
    b = a
    return b

def t_check_not_none(a):
    b = a
    return b

def t_check_same():
    x = [1, 2, 3]
    y = x
    return y

def t_check_not_same():
    x = [1, 2, 3]
    y = list(x)
    return y

def t_multi_given(a, c):
    b = a + c
    return b

def t_three_givens(a, b, c):
    d = a + b + c
    return d

def t_named(a):
    b = a + 1
    return b

def t_tagged(a):
    b = a + 1
    return b

def t_repeated(a):
    b = a + 1
    return b

def t_parameterized(a):
    b = a + 1
    return b

def t_parameterized_mul(a):
    b = a * 2
    return b

def t_assume_true(a):
    b = a + 1
    return b

def t_assume_false(a):
    b = a + 1
    return b

def t_str_concat(a):
    b = a + ' world'
    return b

def t_str_repeat(a):
    b = a * 3
    return b

def t_str_upper(a):
    b = a.upper()
    return b

def t_str_len(a):
    b = len(a)
    return b

def t_str_strip(a):
    b = a.strip()
    return b

def t_str_replace(a):
    b = a.replace('world', 'python')
    return b

def t_list_concat(a):
    b = a + [3]
    return b

def t_list_len(a):
    b = len(a)
    return b

def t_list_sum(a):
    b = sum(a)
    return b

def t_list_sorted(a):
    b = sorted(a)
    return b

def t_list_reversed(a):
    b = list(reversed(a))
    return b

def t_list_slice(a):
    b = a[1:4]
    return b

def t_list_comp(a):
    b = [x * 2 for x in a]
    return b

def t_dict_create(a):
    b = {a: 1}
    return b

def t_dict_len(a):
    b = len(a)
    return b

def t_tuple_create(a, c):
    b = (a, c)
    return b

def t_tuple_len(a):
    b = len(a)
    return b

def t_set_create(a):
    b = set(a)
    return b

def t_bool_and(a):
    b = a > 0 and a < 10
    return b

def t_bool_and_false(a):
    b = a > 0 and a < 10
    return b

def t_bool_or(a):
    b = a > 0 or a < 0
    return b

def t_bool_not(a):
    b = not a
    return b

def t_multi_test(a):
    b = a + 1
    return b

def t_ternary(a):
    b = 'positive' if a > 0 else 'non-positive'
    return b

def t_elif(a):
    if a > 10:
        b = 'large'
    elif a > 0:
        b = 'medium'
    else:
        b = 'small'
    return b

def t_while(a):
    b = 0
    while a > 0:
        b += 1
        a -= 1
    return b

def t_abs(a):
    b = abs(a)
    return b

def t_max(a, c):
    b = max(a, c)
    return b

def t_min(a, c):
    b = min(a, c)
    return b

def t_round(a):
    b = round(a)
    return b

def t_int_cast(a):
    b = int(a)
    return b

def t_str_cast(a):
    b = str(a)
    return b

def t_float_cast(a):
    b = float(a)
    return b

def t_math_sqrt(a):
    b = math.sqrt(a)
    return b

def t_aug_add(a):
    a += 3
    return a

def t_aug_sub(a):
    a -= 3
    return a

def t_aug_mul(a):
    a *= 3
    return a

def t_multi_stmt(a):
    c = 10
    d = 20
    b = a + c + d
    return b

def t_multi_stmt2(a):
    x = 2
    y = 3
    z = 4
    b = a + x + y + z
    return b

def t_chained_cmp(a):
    b = 0 < a < 10
    return b

def t_zero(a):
    b = a * 100
    return b

def t_empty_str(a):
    b = len(a)
    return b

def t_empty_list(a):
    b = len(a)
    return b

def t_negative(a):
    b = a + 3
    return b

def t_large_number(a):
    b = a + 1
    return b

def t_float_arith(a):
    b = a + 0.2
    return b

def t_bool_to_int(a):
    b = int(a)
    return b

def t_for_inner(a):
    b = 0
    for _ in range(a):
        b += 10
    return b

def t_for_if(a):
    b = 0
    for i in range(a):
        if i % 2 == 0:
            b += 1
    return b
