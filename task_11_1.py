import operator
from collections import Counter
from itertools import accumulate
from random import randint

from timer import timer


def swap_tail_head(nums):
    for i in range(len(nums) // 2):
        nums[i], nums[len(nums) // 2 + i + len(nums) % 2] = nums[len(nums) // 2 + i + len(nums) % 2], nums[i]


def has_triplet_sum(nums):
    nums.sort()
    sums = set()
    for i in range(1, len(nums) - 1):
        for j in range(i):
            sums.add(nums[i] + nums[j])
            if nums[i + 1] in sums:
                return True
    return False


def intersection_of_three_lists(nums1, nums2, nums3):
    i = j = k = 0
    result = []
    while i < len(nums1) and j < len(nums2) and k < len(nums3):
        if nums1[i] == nums2[j] and nums2[j] == nums3[k]:
            result.append(nums1[i])
            i += 1
            j += 1
            k += 1
            continue
        n = max(nums1[i], nums2[j], nums3[k])
        if nums1[i] < n:
            i += 1
        if nums2[j] < n:
            j += 1
        if nums3[k] < n:
            k += 1

    return result


def index_of_first_occurrence(s1, s2):
    for i in range(len(s1) - len(s2) + 1):
        if s1[i] == s2[0]:
            for j in range(1, len(s2)):
                if s1[i + j] != s2[j]:
                    break
            else:
                return i
    return -1


def are_equal_after_backspaces(s1, s2):
    def next_letter(s: str, i: int):
        count = 0
        while i >= 0 and s[i] == "#":
            while i >= 0 and s[i] == "#":
                count += 1
                i -= 1

            while i >= 0 and s[i] != "#" and count:
                i -= 1
                count -= 1
        return i

    i1 = len(s1)
    i2 = len(s2)
    while i1 or i2:
        i1 = next_letter(s1, i1 - 1)
        i2 = next_letter(s2, i2 - 1)
        if i1 < 0 and i2 < 0:
            return True
        elif s1[i1] != s2[i2]:
            return False
    return True


def square_and_sort(nums):
    i = 0
    for i in range(len(nums)):
        if nums[i] >= 0:
            break
    j = i - 1
    result = []
    while i < len(nums) and j >= 0:
        if nums[i] ** 2 > nums[j] ** 2:
            result.append(nums[j] ** 2)
            j -= 1
        else:
            result.append(nums[i] ** 2)
            i += 1
    result += [nums[x] ** 2 for x in range(j, -1, -1)]
    result += [nums[x] ** 2 for x in range(i, len(nums))]
    return result


def sort_by_equation(nums, a, b, c):
    result = [0] * len(nums)
    i = 0
    j = - 1
    op = (operator.gt, operator.lt)[a < 0]
    idx_op = (operator.inv, operator.abs)[a < 0]
    for n in range(len(nums)):
        if op(a * nums[i] ** 2 + b * nums[i], a * nums[j] ** 2 + b * nums[j]):
            result[idx_op(n)] = a * nums[i] ** 2 + b * nums[i] + c
            i += 1
        else:
            result[idx_op(n)] = a * nums[j] ** 2 + b * nums[j] + c
            j -= 1
    return result


def segments_intersection(segments1, segments2):
    def intersect(s1, s2):
        a, b = sorted((s1, s2))
        if a[1] >= b[0]:
            return b[0], min(a[1], b[1])
        return None

    i = j = 0
    result = []
    while i < len(segments1) and j < len(segments2):
        seg1 = segments1[i]
        seg2 = segments2[j]
        if seg1[1] > seg2[1]:
            j += 1
        elif seg1[1] < seg2[1]:
            i += 1
        else:
            i += 1
            j += 1

        intersection = intersect(seg1, seg2)
        if intersection:
            result.append(intersection)
    return result


def max_water_container(lines):
    i = 0
    j = len(lines) - 1
    max_volume = 0
    while i < j:
        volume = (j - i) * min(lines[i], lines[j])
        max_volume = max(max_volume, volume)
        if lines[i] > lines[j]:
            j -= 1
        else:
            i += 1
    return max_volume


def count_quadruplets_with_sum(nums, k):
    d = {nums[0]}
    quadruplets = set()
    for a in range(1, len(nums) - 2):
        for b in range(a + 1, len(nums) - 1):
            for c in range(b + 1, len(nums)):
                if k - nums[a] - nums[b] - nums[c] in d:
                    quadruplets.add(tuple(sorted((nums[a], nums[b], nums[c], k - nums[a] - nums[b] - nums[c]))))
        d.add(nums[a])
    return len(quadruplets)


def all_permutations(s1, s2):
    s2_count = Counter(s2)
    s1_count = Counter(s1[:len(s2) - 1])
    result = []
    for i in range(len(s1) - len(s2) + 1):
        s1_count[s1[i + len(s2) - 1]] += 1
        if s1_count == s2_count:
            result.append(i)
        s1_count[s1[i]] -= 1
    return result


def increase_numbers_on_segments(nums, segments, k):
    extra = [0] * (len(nums) + 1)
    for s in segments:
        extra[s[0]] += 1
        extra[s[1] + 1] -= 1
    delta = 0
    for i in range(len(nums)):
        delta += extra[i]
        nums[i] += delta * k


def count_sublists_with_sum(nums, k):
    sums_count = Counter(accumulate(nums, initial=0))
    count = 0
    for i in accumulate(nums, initial=0):
        sums_count[i] -= 1
        if sums_count[i + k] > 0:
            count += sums_count[i + k]
    return count


def count_ways_to_form(s1, s2):
    parts = [0] * len(s2)
    for c in s1:
        for i in range(len(s2) - 1, -1, -1):
            if c == s2[i]:
                parts[i] += parts[i - 1] if i else 1

    return parts[len(s2) - 1]


def count_increasing_triplets(nums):
    count = 0
    for j in range(1, len(nums) - 1):
        less = 0
        greatest = 0
        for i in range(j):
            if nums[i] < nums[j]:
                less += 1
        for k in range(j + 1, len(nums)):
            if nums[k] > nums[j]:
                greatest += 1
        count += less * greatest
    return count


def eulers_conjecture(n=150):
    powers = {i ** 5: i for i in range(1, n)}
    for a in range(4, n):
        for b in range(3, a):
            for c in range(2, b):
                for d in range(1, c):
                    s = a ** 5 + b ** 5 + c ** 5 + d ** 5
                    if s in powers:
                        return a + b + c + d + powers[s]


def eulers_conjecture_mim(n=150):
    abc = {a ** 5 + b ** 5 + c ** 5: (a, b, c) for a in range(3, n) for b in range(2, a) for c in range(1, b)}
    de = {e ** 5 - d ** 5: (d, e) for e in range(2, n) for d in range(1, e)}
    for i in abc:
        if i in de:
            return sum(abc[i]) + sum(de[i])
