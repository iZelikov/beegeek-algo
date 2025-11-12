# def mystery(n):
#     return n**2 - 1
import math


# def mystery(n):
#     return n+2-(n%2)

# def mystery(n):
#     return sum(range(n+1))

def mystery(n):
    d = {'0': 1, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 1, '7': 0, '8': 2, '9': 1}
    result = 0
    for i in str(n):
        result += d[i]
    return result


def sum_of_squares(n):
    return sum([i ** 2 for i in range(n + 1)])


def even_odd(nums: list[int]) -> bool:
    return all([i % 2 == 0 for i in nums]) or all([i % 2 == 1 for i in nums])


def hamming_distance(s1, s2):
    return sum(map(lambda x: x[0] != x[1], zip(s1, s2)))


def longest_substring_without_vowels(s: str) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u']
    n = 0
    n_max = 0
    for c in s:
        if c in vowels:
            n = 0
        else:
            n += 1
            n_max = max(n_max, n)
    return n_max


def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)


def min_digit_sum(a, b):
    digits = [sum_of_digits(i) for i in range(a, b + 1)]
    m = min(digits)
    return digits.count(m)


def avg_values(nums):
    result = []
    s = 0
    for i, n in enumerate(nums, 1):
        s += n
        result.append(s / i)
    return result


def divisible(n):
    total = n
    result = 0
    while n:
        i = n % 10
        n = n // 10
        if i and total % i == 0:
            result += 1
    return result


def is_palindrome_int(n: int):
    # if n < 10:
    #     return True
    # else:
    #     digits = int(math.log10(n))
    #     start = n // 10 ** digits
    #     end = n % 10
    #     crop = n % 10 ** digits // 10
    #     return start == end and is_palindrome_int(crop)
    return n == reverse_int(n)


def reverse_int(n):
    result = 0
    while n:
        result = result * 10 + (n % 10)
        n = n // 10
    return result


def make_palindrome(n, i=0):
    if is_palindrome_int(n):
        return n
    elif i >= 5:
        return -1
    else:
        return make_palindrome(n + reverse_int(n), i + 1)

