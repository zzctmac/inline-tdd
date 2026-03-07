from inline import itest

def t(a):
    itest().given(a, 1).check_eq(b, 2)
    b = a + 1
    return b

def t2(a):
    itest().given(a, 10).check_eq(b, 9)
    if a < 10:
        b = a + 1
    else:
        b = a - 1
    return b