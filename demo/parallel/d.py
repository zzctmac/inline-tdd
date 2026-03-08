from inline_tdd import itestdd
import time

sleep = 0.1
d = 0
d = d + 1
itestdd("1", tag=["add"]).given(d, 1).check_eq(d, 2).check_eq(time.sleep(sleep), None)
itestdd("1", tag=["add"]).given(d, 1).check_eq(d, 2)
itestdd("1", tag=["add"]).given(d, 1).check_eq(d, 2)
d = d + 2
itestdd("2").given(d, 1).check_eq(d, 3).check_eq(time.sleep(sleep), None)
itestdd("2").given(d, 1).check_eq(d, 3)
itestdd("2").given(d, 1).check_eq(d, 3)
d = d - 1
itestdd("3", tag=["minus"]).given(d, 1).check_eq(d, 0).check_eq(time.sleep(sleep), None)
itestdd("3", tag=["minus"]).given(d, 1).check_eq(d, 0)
itestdd("3", tag=["minus"]).given(d, 1).check_eq(d, 0)
