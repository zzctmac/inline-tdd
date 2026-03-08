from inline_tdd import itestdd
import time

sleep = 0.2
c = 0
c = c + 1
itestdd("1", tag=["add"]).given(c, 1).check_eq(c, 2).check_eq(time.sleep(sleep), None)
itestdd("1", tag=["add"]).given(c, 1).check_eq(c, 2)
itestdd("1", tag=["add"]).given(c, 1).check_eq(c, 2)
c = c + 2
itestdd("2").given(c, 1).check_eq(c, 3).check_eq(time.sleep(sleep), None)
itestdd("2").given(c, 1).check_eq(c, 3)
itestdd("2").given(c, 1).check_eq(c, 3)
c = c - 1
itestdd("3", tag=["minus"]).given(c, 1).check_eq(c, 0).check_eq(time.sleep(sleep), None)
itestdd("3", tag=["minus"]).given(c, 1)
itestdd("3", tag=["minus"]).given(c, 1)
