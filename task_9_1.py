from collections import Counter


def count_possible_squares(lines):
    return sum(v // 4 for v in Counter(lines).values())


def sort_by_prod_and_sum(pairs):
    pairs.sort(key=lambda x: (x[0] * x[1], x[0] + x[1]))


def max_profit(prices, k):
    return sum(-i for i in sorted(prices)[:k] if i < 0)


def sort_by_value_and_index(nums):
    extra = sorted((i * v, v) for i, v in enumerate(nums, 1))
    for i in range(len(nums)):
        nums[i] = extra[i][1]


def most_frequent_digit_length(nums):
    return max(Counter(len(str(i)) for i in nums).items(), key=lambda x: (x[1], x[0]))[0]


def sum_of_products(nums):
    l = sorted(nums)
    return sum(l[i] * l[~i] for i in range(len(nums) // 2))


def max_sum_of_products(nums1, nums2):
    n1 = sorted(nums1)
    n2 = sorted(nums2)
    return sum(n1[i] * n2[i] for i in range(len(nums1)))


def min_steps_to_sort(nums):
    prev = float('-inf')
    steps = 0
    for i in nums:
        if i <= prev:
            steps += prev - i + 1
            prev += 1
        else:
            prev = i
    return steps


def sort_only_positives(nums):
    pos = iter(sorted(i for i in nums if i > 0))
    for i in range(len(nums)):
        if nums[i] > 0:
            nums[i] = next(pos)

def is_permutation(nums):
    return set(nums) == set(range(1,len(nums)+1))
