def check_letters(s: str) -> str:
    result = [0] * 26
    for c in s:
        x = ord(c.lower()) - 96
        if 1 <= x <= 26:
            result[x - 1] = 1
    return ''.join(map(str, result))


def find_peaks(nums):
    return sum(nums[i - 1] < nums[i] > nums[i + 1] for i in range(1, len(nums) - 1))


def kth_occurrence(nums, target, k):
    count = 0
    for i, v in enumerate(nums):
        if v == target:
            count += 1
            if count == k:
                return i
    return -1


def find_sum_indexes(nums, value):
    start = 0
    s = 0
    for i, n in enumerate(nums):
        s += n
        while s > value and start < i:
            s -= nums[start]
            start += 1
        if s == value:
            return start, i
    return -1


def sequence_type(nums):
    result = {
        'CONSTANT': 1,
        'ASCENDING': 1,
        'DESCENDING': 1,
        'WEAKLY ASCENDING': 1,
        'WEAKLY DESCENDING': 1,
    }
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            result['CONSTANT'] = 0
        if nums[i] <= nums[i - 1]:
            result["ASCENDING"] = 0
        if nums[i] < nums[i - 1]:
            result["WEAKLY ASCENDING"] = 0
        if nums[i] >= nums[i - 1]:
            result["DESCENDING"] = 0
        if nums[i] > nums[i - 1]:
            result["WEAKLY DESCENDING"] = 0

    for k, v in result.items():
        if v:
            return k
    return "RANDOM"


def lowercase_before_uppercase(s: str) -> bool:
    if len(s) > 1:
        for i in range(1, len(s)):
            if s[i].islower() and s[i - 1].isupper():
                return False
    return True


def add_one(digits):
    result = digits[:]
    last = -1
    while result[last] == 9:
        result[last] = 0
        last -= 1
        if last < - len(result):
            result = [0] + result
    result[last] += 1
    return result


def drop_digit(digits):
    for i in range(1, len(digits)):
        if digits[i - 1] < digits[i]:
            return digits[:i - 1] + digits[i:]
    return digits[:-1]


adjacent_parity = lambda nums: abs(len(nums) - 2 * sum(i % 2 for i in nums)) in (0, 1, len(nums))


def is_possible_to_split(nums):
    return len(set(nums)) in (1, 2)


def find_majority_element(nums):
    major = nums[0]
    count = 0
    for num in nums:
        if count == 0:
            major = num
            count += 1
        elif num == major:
            count += 1
        elif num != major:
            count -= 1

    if sum(i == major for i in nums) > len(nums) // 2:
        return major
    return -1


def count_divisible_pairs(nums):
    div13 = sum(i % 13 == 0 for i in nums)
    return div13 * (len(nums) - 1) - div13 * (div13 - 1) // 2
