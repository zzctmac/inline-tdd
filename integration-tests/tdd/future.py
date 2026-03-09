from __future__ import unicode_literals
from inline_tdd import itestdd

def future_concat(a, b):
    itestdd().given(a, "1").given(b, "2").check_eq(c, "12")
    c = a + b
