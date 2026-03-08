from inline_tdd import itestdd
from collections import deque, defaultdict

# ============================================================
# Quick Sort
# ============================================================

def _partition(arr, low, high):
    itestdd().given(arr, [3, 6, 1, 8, 2]).given(low, 0).given(high, 4).check_eq(pivot, 2)
    pivot = arr[high]
    itestdd().given(low, 1).check_eq(i, 0)
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low=None, high=None):
    if low is None:
        low = 0
        high = len(arr) - 1
    if low < high:
        itestdd().given(arr, [3, 6, 1, 8, 2]).given(low, 0).given(high, 4).check_eq(pi, 1)
        pi = _partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)
    return arr


print(_partition([3, 6, 1, 8, 2], 0, 4))
print(quicksort([3, 6, 1, 8, 2]))