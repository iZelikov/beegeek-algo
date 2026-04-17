import operator
from itertools import accumulate, pairwise, starmap, chain


def product_in_segments(nums, segments):
    pref = list(accumulate(nums, func=operator.mul, initial=1))
    return [pref[segment[1] + 1] // pref[segment[0]] for segment in segments]


def restore_by_prefix_sum(nums):
    return [b - a for a, b in pairwise(nums)]


def min_valid_index(nums, k, m):
    pref = list(accumulate(nums, initial=0))
    for i in range(0, len(nums) - k):
        if pref[i + k + 1] - pref[i] == m:
            return i
    return -1


def difference_list(nums):
    pref = list(accumulate(nums, initial=0))
    return [abs(pref[-1] - pref[i] - pref[i - 1]) for i in range(1, len(pref))]


def zeros_in_segments(nums, segments):
    pref = list(accumulate(nums, func=lambda a, b: a + (b == 0), initial=0))
    return [pref[s[1] + 1] - pref[s[0]] for s in segments]


def valid_nums_in_segments(nums, segments):
    pref = list(
        map(lambda x: x[0], accumulate(nums, func=lambda a, b: (a[0] + (b > a[1]), b), initial=(0, float('inf')))))
    return [pref[s[1] + 1] - pref[s[0] + 1] for s in segments]


def difference_list(nums):
    pref = list(accumulate(nums, initial=0))
    return [abs(nums[i] * i - pref[i]) + abs(nums[i] * (len(nums) - i) - (pref[-1] - pref[i])) for i in
            range(len(nums))]


def sum_in_rectangles(matrix, rectangles):
    pref = [list(accumulate(m, initial=0)) for m in matrix]
    return [sum(pref[i][r[1][1] + 1] - pref[i][r[0][1]] for i in range(r[0][0], r[1][0] + 1)) for r in rectangles]


def has_sublist_with_sum(nums, k):
    pref = {0}
    s = 0
    for n in nums:
        s += n
        if s - k in pref:
            return True
        pref.add(s)
    return False
