from inline_tdd import itestdd
import time

sleep = 0.1
b = 0
b = b + 1
itestdd("1", tag=["add"]).given(b, 1).check_eq(b, 2).check_eq(time.sleep(sleep), None)
itestdd("1", tag=["add"]).given(b, 1).check_eq(b, 2)
itestdd("1", tag=["add"]).given(b, 1).check_eq(b, 2)
b = b + 2
itestdd("2").given(b, 1).check_eq(b, 3).check_eq(time.sleep(sleep), None)
itestdd("2").given(b, 1).check_eq(b, 3)
itestdd("2").given(b, 1).check_eq(b, 3)
b = b - 1
itestdd("3", tag=["minus"]).given(b, 1).check_eq(b, 0).check_eq(time.sleep(sleep), None)
itestdd("3", tag=["minus"]).given(b, 1).check_eq(b, 0)
itestdd("3", tag=["minus"]).given(b, 1).check_eq(b, 0)
