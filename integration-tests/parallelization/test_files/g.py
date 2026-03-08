from inline_tdd import itestdd
import time

sleep = 2
g = 0
itestdd("1", tag=["add"]).given(g, 1).check_eq(g, 2).check_eq(time.sleep(sleep), None)
itestdd("1", tag=["add"]).given(g, 1).check_eq(g, 2)
itestdd("1", tag=["add"]).given(g, 1).check_eq(g, 2)
g = g + 1
itestdd("2").given(g, 1).check_eq(g, 3).check_eq(time.sleep(sleep), None)
itestdd("2").given(g, 1).check_eq(g, 3)
itestdd("2").given(g, 1).check_eq(g, 3)
g = g + 2
itestdd("3", tag=["minus"]).given(g, 1).check_eq(g, 0).check_eq(time.sleep(sleep), None)
itestdd("3", tag=["minus"]).given(g, 1).check_eq(g, 0)
itestdd("3", tag=["minus"]).given(g, 1).check_eq(g, 0)
g = g - 1
