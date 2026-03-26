def max_digit(num):
    m = 0
    while num > 0:
        d = num % 10
        num = num // 10
        if d >= m:
            m = d
    return m


def max_of_two(a, b):
    return max(a, b)


def max_of_four(a, b, c, d):
    return max_of_two(max_of_two(a, b), max_of_two(c, d))


def golden_pairs(pairs):
    return sum(1.6 <= max(i) / min(i) <= 1.7 for i in pairs)


def min_max_diff(nums):
    return max(nums) - min(nums)


def can_nest(nums1, nums2):
    return min(nums1) > min(nums2) and max(nums1) < max(nums2) or min(nums1) < min(nums2) and max(nums1) > max(nums2)


def max_to_min(nums):
    mx = max(nums)
    mn = min(nums)
    for i, v in enumerate(nums):
        if v == mx:
            nums[i] = mn


def get_oldest(ages: dict):
    return min(ages.items(), key=lambda x: (-x[1], x[0]))[0]


def max_value(strings):
    def x(s: str):
        if s.isdigit():
            return int(s)
        else:
            return len(s)

    return x(max(strings, key=x))


def min_even_digit(num):
    m = 9
    while num > 0:
        d = num % 10
        num = num // 10
        if d <= m and d % 2 == 0:
            m = d
    return (-1, m)[m < 9]


def max_digits_sum(nums):
    def sum_dig(num: int) -> tuple[int, int]:
        n = abs(num)
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        return s, num

    return max(nums, key=sum_dig)


def max_nearby_product(nums):
    m = float('-inf')
    for i in range(1, len(nums)):
        m = max(nums[i - 1] * nums[i], m)
    return m


def find_index_of_max(nums, reverse=False):
    m = float('-inf')
    idx = None
    for i in range(len(nums)):
        x = (i, len(nums) - i - 1)[reverse]
        if nums[x] > m:
            m = nums[x]
            idx = x
    return idx


def find_number(nums):
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1

    l = []
    for k, v in d.items():
        if k == v:
            l.append(k)

    if l:
        return max(l)
    else:
        return -1


def max_consecutive_ones(nums):
    max_ones = 0
    ones = 0
    for i in nums:
        if i == 1:
            ones += 1
            if ones > max_ones:
                max_ones = ones
        else:
            ones = 0
    return max_ones


def max_sum(nums):
    m = max(nums)
    return (sum(i for i in nums if i > 0), m)[m <= 0]


