from inline_tdd import itestdd
import time

sleep = 1
h = 0
itestdd("1", tag=["add"]).given(h, 1).check_eq(h, 2).check_eq(time.sleep(sleep), None)
itestdd("1", tag=["add"]).given(h, 1).check_eq(h, 2)
itestdd("1", tag=["add"]).given(h, 1).check_eq(h, 2)
h = h + 1
itestdd("2").given(h, 1).check_eq(h, 3).check_eq(time.sleep(sleep), None)
itestdd("2").given(h, 1).check_eq(h, 3)
itestdd("2").given(h, 1).check_eq(h, 3)
h = h + 2
itestdd("3", tag=["minus"]).given(h, 1).check_eq(h, 0).check_eq(time.sleep(sleep), None)
itestdd("3", tag=["minus"]).given(h, 1).check_eq(h, 0)
itestdd("3", tag=["minus"]).given(h, 1).check_eq(h, 0)
h = h - 1
