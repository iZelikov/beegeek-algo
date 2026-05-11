import operator
from functools import reduce


def sum_powers_of_two(n, m):
    return (1 << n) + (1 << m)


def is_power_of_two(num):
    return not (num - 1) & num


def reset_last_k_bits(num, k):
    return num >> k << k


def rightmost_set_bit(num):
    i = 0
    while num:
        if num & 1:
            return i
        num >>= 1
        i += 1


def reset_last_set_bit(num):
    return (num & -num) ^ num


def count_reset_bits(num: int):
    return num.bit_length() - num.bit_count()


def bit_difference(num1, num2):
    return (num1 ^ num2).bit_count()


def left_cyclic_shift(num, k):
    return (num << k | num >> 8 - k) & 255


def encrypt(num):
    return ~43690 & (num >> 1) | 43690 & (num << 1)


def xor_encrypt(m, k):
    return "".join(chr(ord(m[i]) ^ ord(k[i % len(k)])) for i in range(len(m)))


def max_xor_excluding_one(nums):
    a = reduce(operator.xor, nums)
    return max(a ^ i for i in nums)


def extra_num(nums):
    return reduce(operator.xor, nums)


def roman_to_arabic(roman_num):
    romans = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9,
              "V": 5, "IV": 4, "I": 1}
    i = 0
    num = 0
    for r in romans:
        while roman_num[i:i + len(r)] == r:
            num += romans[r]
            i += len(r)
    return num


def arabic_to_roman(num):
    romans = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
              5: 'V', 4: 'IV', 1: 'I'}
    roman_num = []
    for r in romans:
        while num >= r:
            roman_num.append(romans[r])
            num -= r
    return "".join(roman_num)
