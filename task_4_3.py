import re
from itertools import pairwise


def fizz_buzz(n):
    return [(i, 'Fizz', 'Buzz', 'FizzBuzz')[(i % 3 == 0) + 2 * (i % 5 == 0)] for i in range(1, n + 1)]


def one_truth(flags: list[bool]):
    return flags.count(True) == 1


def parse_max(s):
    return max(map(int, re.findall(r'\d+', s)), default=-1)


def equilibrium(nums: list[int]):
    right_sum = sum(nums)
    left_sum = 0
    for i, item in enumerate(nums):
        right_sum -= item
        if left_sum == right_sum:
            return i
        else:
            left_sum += item
    return -1


def letter_by_sum(letters: list[str]):
    return chr((sum(map(lambda c: (ord(c) - ord('a') + 1), letters)) - 1) % 26 + ord('a'))


def is_perfect_possible(key: list[str], answers: list[str]):
    result = [k == a for k, a in zip(key, answers) if k != '*']
    return all(result) or not any(result)


def count_animals(heads, legs) -> tuple[int, int] | None:
    r = legs / 2 - heads
    if r.is_integer() and 0 <= r <= heads:
        return int(heads - r), int(r)
    return None


def is_order(nums: list[int], strict=True):
    asc = True
    desc = True
    for a, b in pairwise(nums):
        if a < b:
            desc = False
        elif a > b:
            asc = False
        elif strict:
            asc = desc = False

        if not asc and not desc:
            return False
    return True


def wave(nums: list[int]):
    nums[:-(len(nums) % 2) or None:2], nums[1::2] = nums[1::2], nums[:-(len(nums) % 2) or None:2]


def count_days(cur: int):
    n = 0
    while cur % 2:
        n += 1
        cur = (cur - 1) // 2
    return n