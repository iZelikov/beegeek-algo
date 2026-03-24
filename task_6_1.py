def linear_search(nums, target, reverse=False):
    for i in range(len(nums)):
        if reverse:
            if nums[~i] == target:
                return len(nums) - 1 - i
        else:
            if nums[i] == target:
                return i
    return -1


def equal(nums):
    for i, v in enumerate(nums):
        if v == i:
            return i
    return -1


def search_insert_position(nums, target):
    for i, v in enumerate(nums):
        if v >= target:
            return i
    return len(nums)


def count_numbers(n: int, k: int) -> int:
    count = 0
    for i in range(1, n + 1):
        if i - sum(map(int, str(i).strip())) >= k:
            count += 1
    return count


def nine_divisors(n: int) -> int:
    numbers = 0
    for i in range(6, round(n ** 0.5) + 1):
        divisors = 0
        for j in range(2, i):
            if i ** 2 % j == 0:
                divisors += 1
            if divisors > 3:
                break
        if divisors == 3:
            numbers += 1
    return numbers


def find_number(nums):
    for i in range(1, len(nums), 2):
        if nums[i] != nums[i - 1]:
            return nums[i - 1]
    return nums[-1]


def doubling_the_value(nums: list[int], value: int) -> int:
    for num in nums:
        if num == value:
            value *= 2
    return value


count_occurrences = lambda nums, target, start, end: sum(1 for i in range(start, end) if nums[i] == target)


def elements_in_the_range(nums: list[int], start: int, end: int):
    return set(range(start, end + 1)) == set(i for i in nums if start <= i <= end)
