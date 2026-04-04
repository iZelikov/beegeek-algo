def missing_number(n, nums):
    return (1 + n) * n // 2 - sum(nums)


from collections import Counter


def find_number(nums):
    d = Counter(nums)
    for k, v in d.items():
        if v == 1:
            return k


def shortest_distance(x, y, z):
    v1 = 2 * x + 2 * y
    v2 = 2 * x + 2 * z
    v3 = 2 * y + 2 * z
    v4 = x + y + z
    return min(v1, v2, v3, v4)


def smallest_missing_positive(nums):
    p = 1
    p_old = 1
    while True:
        for i in range(len(nums)):
            if nums[i] == p:
                p += 1
        if p == p_old:
            return p
        else:
            p_old = p


def find_max_ratio(nums):
    m = nums[0]
    ratio = 1
    for i in nums:
        if i < m:
            m = i
        else:
            if i / m > ratio:
                ratio = i / m
    return (-1, ratio)[ratio > 1]


def find_point(lines):
    right = min(lines, key=lambda x: x[1])
    left = max(lines, key=lambda x: x[0])
    if left[0] <= right[1]:
        return left[0]


def closest_point(radius, points):
    r2 = radius ** 2
    dist2 = lambda p: p[0] ** 2 + p[1] ** 2
    sort_key = lambda p: (dist2(p), p[0], p[1])
    predicate = lambda p: dist2(p) > r2
    return min(filter(predicate, points), key=sort_key, default=None)


def count_ones(nums):
    left = rl = 0
    right = lr = len(nums) - 1
    while left < lr or right > rl:
        mid = left + (lr - left) // 2
        if nums[left] >= 1:
            lr = left
        elif nums[mid] < 1:
            left = mid + 1
        else:
            lr = mid
            left += 1

        mid = rl + (right - rl) // 2
        if nums[right] <= 1:
            rl = right
        elif nums[mid] > 1:
            right = mid - 1
        else:
            rl = mid
            right - +1
    return (0, right - left + 1)[nums[left] == 1 and nums[right] == 1]


def first_even(nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[left] % 2 == 0:
            return left
        elif nums[mid] % 2:
            left = mid + 1
        else:
            right = mid


def move_min_elements(nums):
    m = min(nums)
    n = 0
    for i in range(len(nums)):
        if nums[~i] == m:
            n += 1
        else:
            nums[~i + n] = nums[~i]
            if len(nums) - i <= n:
                nums[~i] = m


import math


def days_for_solve(n, k):
    return math.ceil((((2 * k - 1) ** 2 + 8 * n) ** 0.5 - 2 * k - 1) / 2) + 1


# def missing_numbers(n, nums):
#     extra = [0, 0]
#     result = []
#     i = 0
#     while i < n - 2:
#         k = nums[i] - 1
#         if k < n - 2:
#             if k >= 0 and k != i:
#                 nums[i], nums[k] = nums[k], nums[i]
#             else:
#                 i += 1
#         else:
#             nums[i], extra[k - n] = extra[k - n], nums[i]
#             i += 1
#     for i, v in enumerate(nums):
#         if v == 0:
#             result.append(i + 1)
#     for i, v in enumerate(extra, n - 2):
#         if v == 0:
#             result.append(i + 1)
#     return tuple(result)


def missing_numbers(n, nums):
    if not nums:
        return 1, 2
    nums += 3*[0]

    for i in range(1, n + 1):
        while (nums[i] != i) and (nums[nums[i]] != nums[i]):
            tmp = nums[i]
            nums[i] = nums[tmp]
            nums[tmp] = tmp
    ans = []
    for i in range(1, n + 1):
        if nums[i] != i:
            ans.append(i)
    ans.sort()
    print(nums)
    return ans[0], ans[1]

data = [1,4]
print(missing_numbers(4, data))
print(data)