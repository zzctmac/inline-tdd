from inline_tdd import itestdd
import time

sleep = 2
i = 0
itestdd("1", tag=["add"]).given(i, 1).check_eq(i, 2).check_eq(time.sleep(sleep), None)
itestdd("1", tag=["add"]).given(i, 1).check_eq(i, 2)
itestdd("1", tag=["add"]).given(i, 1).check_eq(i, 2)
i = i + 1
itestdd("2").given(i, 1).check_eq(i, 3).check_eq(time.sleep(sleep), None)
itestdd("2").given(i, 1).check_eq(i, 3)
itestdd("2").given(i, 1).check_eq(i, 3)
i = i + 2
itestdd("3", tag=["minus"]).given(i, 1).check_eq(i, 0).check_eq(time.sleep(sleep), None)
itestdd("3", tag=["minus"]).given(i, 1).check_eq(i, 0)
itestdd("3", tag=["minus"]).given(i, 1).check_eq(i, 0)
i = i - 1
