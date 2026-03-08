from inline_tdd import itestdd
import time

sleep = 2
e = 0
itestdd("1", tag=["add"]).given(e, 1).check_eq(e, 2).check_eq(time.sleep(sleep), None)
itestdd("1", tag=["add"]).given(e, 1).check_eq(e, 2)
itestdd("1", tag=["add"]).given(e, 1).check_eq(e, 2)
e = e + 1
itestdd("2").given(e, 1).check_eq(e, 3).check_eq(time.sleep(sleep), None)
itestdd("2").given(e, 1).check_eq(e, 3)
itestdd("2").given(e, 1).check_eq(e, 3)
e = e + 2
itestdd("3", tag=["minus"]).given(e, 1).check_eq(e, 0).check_eq(time.sleep(sleep), None)
itestdd("3", tag=["minus"]).given(e, 1).check_eq(e, 0)
itestdd("3", tag=["minus"]).given(e, 1).check_eq(e, 0)
e = e - 1
