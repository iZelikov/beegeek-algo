import math
from collections import Counter
from itertools import groupby, pairwise


def find_triple(nums):
    nums.sort()
    return sorted((nums[3] - nums[2], nums[3] - nums[1], nums[3] - nums[0]))


def max_sum_of_k_elements(nums, k):
    nums.sort(reverse=True)
    return sum(nums[:k])


def count_mismatches(nums):
    s = sorted(nums)
    return sum(nums[i] != s[i] for i in range(len(nums)))


def sort_by_length_and_value(nums):
    nums.sort(key=lambda x: (-math.floor(math.log10(abs(x))) if x else 0, x))


def holey_sort(nums):
    holes = {0: 1, 6: 1, 8: 2, 9: 1}

    def key(x):
        s = 0
        n = abs(x)
        while True:
            s += holes.get(n % 10, 0)
            n //= 10
            if not n:
                break
        return s, x

    nums.sort(key=key)


def are_anagram(s1, s2):
    return Counter(s1) == Counter(s2)


def priority_sort(nums, priority_nums):
    nums.sort(key=lambda x: (x not in priority_nums, x))


def advanced_sort(nums):
    return [list(g) for k, g in groupby(sorted(nums))]


def largest_gap(nums):
    dif = max(pairwise(sorted(nums)), key=lambda x: x[1] - x[0])
    return dif[1] - dif[0]


def max_possible_number(nums1, nums2):
    result = sorted((Counter(nums1) & Counter(nums2)).elements(), reverse=True)
    return int("".join(map(str, result))) if result else -1


def alternate_sort(data):
    data.sort(key=lambda x: (isinstance(x, str), x))
    data[::2], data[1::2] = data[:len(data) // 2], data[len(data) // 2:]


def odd_even_sort(nums):
    nums.sort(key=lambda x: (not x % 2, x * (x % 2 * 2 - 1)))


def find_difference(s1, s2):
    return next((Counter(s2) - Counter(s1)).elements())


def ranks_of_elements(nums):
    ranks = {v: i for i, v in enumerate(sorted(set(nums)), 1)}
    return [ranks[i] for i in nums]


def length_of_painted_part(lines):
    sorted_lines = sorted(lines)
    start = end = sorted_lines[0][0]
    length = 0
    for line in sorted_lines:
        if line[0] <= end:
            end = max(end, line[1])
        else:
            length += end - start
            start = line[0]
            end = line[1]
    return length + (end - start)


def remove_covered_segments(segments):
    sorted_segments = sorted(segments, key=lambda x: (x[0], -x[1]))
    cover = sorted_segments[0]
    count_covered = -1
    for s in sorted_segments:
        if cover[1] >= s[1]:
            count_covered += 1
        else:
            cover = s
    return len(segments) - count_covered


import operator


def is_almost_sorted(nums):
    def check_anomaly(op):
        if 1 < i < len(nums) - 1 and op(nums[i - 2], nums[i]) and op(nums[i - 1], nums[i + 1]):
            return 2
        return 1

    asc_anomaly = 0
    desc_anomaly = 0
    for i in range(1, len(nums)):
        if desc_anomaly < 2 and nums[i - 1] < nums[i]:
            desc_anomaly += check_anomaly(operator.lt)
        if asc_anomaly < 2 and nums[i - 1] > nums[i]:
            asc_anomaly += check_anomaly(operator.gt)
        if min(asc_anomaly, desc_anomaly) > 1:
            return False
    return True
