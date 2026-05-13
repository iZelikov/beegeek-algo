import operator
import string
from functools import reduce


def bin_to_hex(binary_str):
    return f"{int(binary_str, 2):X}"


def oct_to_bin(oct_str):
    return f"{int(oct_str, 8):b}"


def is_double_base_palindrome(num, p):
    def is_palindrome(base=10):
        digits = []
        n = num
        while n:
            digits.append(n % base)
            n //= base
        return all(first == last for first, last in zip(digits, reversed(digits)))

    return is_palindrome(10) and is_palindrome(p)


def column_number(title):
    digits = {c: i for i, c in enumerate(string.ascii_uppercase, 1)}
    return sum(len(digits) ** i * digits[c] for i, c in enumerate(reversed(title)))


def longest_ones_with_one_flip(num):
    left = right = 0
    max_1 = 0
    for n in f'{num:b}':
        if n == '1':
            right += 1
        else:
            max_1 = max(left + right, max_1)
            left, right = right, 0
    return max(left + right, max_1) + 1


def set_last_reset_bit(num):
    return num | num + 1


def leave_last_k_bits(num, k):
    return (num >> k << k) ^ num


def max_power_of_two_divisor(num):
    return ((num ^ num - 1) + 1) >> 1


def extra_num(n, nums):
    # return sum(nums) - n * (n + 1) // 2
    return reduce(operator.xor, nums, reduce(operator.xor, range(1, n + 1)))


def all_binary_strings(n):
    return [f'{i:0{n}b}' for i in range(1 << n)]


def filter_and_sort_even_numbers(nums):
    return sorted(filter(lambda n: not n & 1 and (n >> 6) & 1, nums))


def super_xor(n):
    return (n, 1, n + 1, 0)[n % 4]


def extra_nums(nums):
    xor_a_b = reduce(operator.xor, nums)
    diff = xor_a_b & -xor_a_b
    a = reduce(operator.xor, (i for i in nums if i & diff))
    b = xor_a_b ^ a
    return a, b
