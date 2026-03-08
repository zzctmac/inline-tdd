from inline_tdd import itestdd
import time

sleep = 1
f = 0
itestdd("1", tag=["add"]).given(f, 1).check_eq(f, 2).check_eq(time.sleep(sleep), None)
itestdd("1", tag=["add"]).given(f, 1).check_eq(f, 2)
itestdd("1", tag=["add"]).given(f, 1).check_eq(f, 2)
f = f + 1
itestdd("2").given(f, 1).check_eq(f, 3).check_eq(time.sleep(sleep), None)
itestdd("2").given(f, 1).check_eq(f, 3)
itestdd("2").given(f, 1).check_eq(f, 3)
f = f + 2
itestdd("3", tag=["minus"]).given(f, 1).check_eq(f, 0).check_eq(time.sleep(sleep), None)
itestdd("3", tag=["minus"]).given(f, 1).check_eq(f, 0)
itestdd("3", tag=["minus"]).given(f, 1).check_eq(f, 0)
f = f - 1
