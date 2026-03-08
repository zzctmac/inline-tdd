from inline_tdd import itestdd

a = 0
a = a + 1
itestdd("1", tag=["add"]).given(a, 1).check_eq(a, 2)
itestdd("1", tag=["add"]).given(a, 1).check_eq(a, 2)
itestdd("1", tag=["add"]).given(a, 1).check_eq(a, 2)
a = a + 2
itestdd("2").given(a, 1).check_eq(a, 3)
itestdd("2").given(a, 1).check_eq(a, 3)
itestdd("2").given(a, 1).check_eq(a, 3)
a = a - 1
itestdd("3", tag=["minus"]).given(a, 1).check_eq(a, 0)
itestdd("3", tag=["minus"]).given(a, 1).check_eq(a, 0)
itestdd("3", tag=["minus"]).given(a, 1).check_eq(a, 0)
