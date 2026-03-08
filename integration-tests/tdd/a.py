from inline import itest

def t(a):
    itest().given(a, 1).check_eq(b, 2)
    b = a + 1
    return b

def t2(a):
    itest().given(a, 10).check_eq(b, 9)
    itest().given(a, 1).check_eq(b, 2)
    if a < 10:
        itest().given(a, 1).check_eq(b, 2)
        b = a + 1
    else:
        #itest().given(a, 0).check_eq(b, -1)
        b = a - 1
    return b

def t3(a):
    b = 0
    itest().given(a, 3).check_eq(b, 6)
    itest().given(a, 0).check_eq(b, 0)
    itest().given(a, 1).check_eq(b, 2)
    for _ in range(a):
        itest().given(b, 3).check_eq(b, 5)
        b += 2
    return b
