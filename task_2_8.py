from math import *


def count_digits(n: int) -> int:
    return int(log10(n)) + 1


def is_power_of_two(n: int) -> bool:
    return log2(n).is_integer()


def closest_exponent(n: int) -> int:
    return ceil(log2(n))


def iterated_log(n: int) -> int:
    i = 0
    while n > 1:
        i += 1
        n = log2(n)
    return i


def count_powers(num: int) -> int:
    n = 0
    while num > 1:
        n += 1
        num %= 2**n * 10**(int(log10(num))-int(log10(2**n)))
    return n
