import itertools
from collections import Counter


def smallest_palindrome(s):
    return "".join(min(s[i], s[~i]) for i in range(len(s)))


def has_triplet_with_zero_sum(nums):
    n = Counter(nums)
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            a = nums[i]
            b = nums[j]
            c = -(a + b)
            c_n = n[- nums[i] - nums[j]]
            if c_n == 0:
                continue
            elif a == b and b == c and c_n < 3:
                continue
            elif (a == c or b == c) and n[- nums[i] - nums[j]] < 2:
                continue
            else:
                return True
    return False


def min_difference(nums1, nums2):
    n1 = sorted(nums1)
    n2 = sorted(nums2)
    i = 0
    j = 0
    min_dif = float('inf')
    while i < len(n1) and j < len(n2):
        min_dif = min(min_dif, abs(n1[i] - n2[j]))
        if n1[i] < n2[j]:
            i += 1
        elif n1[i] > n2[j]:
            j += 1
        else:
            return 0
    return min_dif


def count_pairs_with_greater_difference(nums, k):
    i = 0
    j = 1
    count = 0
    while j < len(nums):
        if nums[j] - nums[i] > k:
            count += len(nums) - j
            i += 1
        else:
            j += 1
    return count


def pair_with_lower_or_equal_difference(nums, k):
    if len(nums) < 2:
        return None
    i = 0
    j = 1
    max_diff = (i, j, nums[j] - nums[i])
    while j < len(nums):
        diff = nums[j] - nums[i]
        if i == j:
            j += 1
        elif diff == k:
            return nums[i], nums[j]
        elif diff > k:
            i += 1
        elif diff > max_diff[2]:
            max_diff = (i, j, diff)
            j += 1
        else:
            j += 1
    return (None, (nums[max_diff[0]], nums[max_diff[1]]))[max_diff[2] <= k]


def count_rescue_attempts(weights, limit):
    weights.sort()
    i = 0
    j = len(weights) - 1
    attempts = 0
    while i <= j:
        if weights[i] + weights[j] <= limit:
            i += 1
        j -= 1
        attempts += 1
    return attempts


def number_of_cinemas(times):
    starts = sorted(times)
    ends = sorted(times, key=lambda x: x[1])
    max_cinemas = 0
    occupied = 0
    i = j = 0
    while i < len(times) and j < len(times):
        if starts[i][0] < ends[j][1]:
            i += 1
            occupied += 1
        else:
            j += 1
            occupied -= 1
        max_cinemas = max(max_cinemas, occupied)
    return max_cinemas


def count_triplets_with_lower_sum(nums, value):
    nums.sort()
    triplets = 0
    for i in range(len(nums) - 2):
        k = i + 1
        j = len(nums) - 1
        while k < j:
            if nums[i] + nums[j] + nums[k] < value:
                triplets += j - k
                k += 1
            else:
                j -= 1
    return triplets


def len_of_shortest_unsorted_part(nums):
    if len(nums) < 2:
        return 0
    i = 0
    j = len(nums) - 1
    while i < j and nums[i] < nums[i + 1]:
        i += 1

    while j >= i and nums[j] > nums[j - 1]:
        j -= 1

    mx = max((nums[x] for x in range(i, j + 1)), default=nums[j])
    mn = min((nums[x] for x in range(i, j + 1)), default=nums[i])

    while i >= 0:
        if nums[i] < mn:
            break
        i -= 1

    while j < len(nums):
        if nums[j] > mx:
            break
        j += 1

    return j - i - 1
