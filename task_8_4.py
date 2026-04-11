from collections import Counter


def count_triplet_numbers(nums):
    return sum(v == 3 for v in Counter(nums).values())


def least_frequent_number(nums):
    l = [0] * 1000
    for i in nums:
        l[i - 1] += 1

    mn = float('inf')
    mi = 0
    for i, v in enumerate(l):
        if v and v < mn:
            mn = v
            mi = i
    return mi + 1


def count_beautiful_pairs(nums):
    return sum(n // 2 for n in Counter(nums).values())


def sort_binary_list(binary_list: list[int]):
    d = Counter(binary_list)
    for i in range(d[0]):
        binary_list[i] = 0
    for i in range(d[1]):
        binary_list[~i] = 1


def sort_limited_numbers(nums):
    d = sorted(Counter(nums).items(), reverse=True)
    n = 0
    for v, count in d:
        while count:
            nums[n] = v
            n += 1
            count -= 1


def is_subset(s1, s2):
    return Counter(s1) <= Counter(s2)


def count_pairs(nums):
    return sum((n + 1) * n // 2 for n in Counter(nums).values())


def max_common_sum(nums):
    return max(Counter(n % 10 + (n // 10) % 10 for n in nums).items(), key=lambda x: (x[1], x[0]))[0]


def count_pairs_divisible_by_three(nums):
    d = Counter(n % 3 for n in nums)
    return d[1] * d[2] + (d[0] - 1) * d[0] // 2


def longest_palindrome(s):
    d = Counter(s)
    min_even = min(filter(lambda x: x[1] % 2, d.items()), default=('', 0))[0]
    result = [i[0] * (i[1] // 2) for i in sorted(d.items())]
    return ''.join(result) + min_even + ''.join(result[::-1])
