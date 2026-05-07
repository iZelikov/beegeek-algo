from task_6_3 import max_sum


def sum_of_digits_in_base(num, base):
    result = 0
    while num:
        result += num % base
        num //= base
    return result


def from_decimal(num, base):
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    while num > 0:
        result.append(digits[num % base])
        num //= base
    return ''.join(reversed(result)) or '0'


def convert_base(str_num, from_base, to_base):
    decimal = 0
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d_dict = {v: i for i, v in enumerate(digits)}
    for i, d in enumerate(reversed(str_num)):
        decimal += from_base ** i * d_dict[d]

    result = []
    while decimal > 0:
        result.append(digits[decimal % to_base])
        decimal //= to_base
    return ''.join(reversed(result)) or '0'


def count_good_numbers(nums):
    count = 0
    for n in nums:
        dec_good = False
        d = n
        while d:
            if d % 10 == 8:
                dec_good = True
                break
            d //= 10
        hex_good = n % 16 == 4 and n >= 256
        count += hex_good and dec_good
    return count


def binary_shift_game_result(num):
    b_num = []
    while num:
        b_num.append(num % 2)
        num //= 2
    b_num.reverse()
    max_num = b_num
    for _ in range(len(b_num)):
        b_num = [b_num[-1]] + b_num[:-1]
        max_num = max(max_num, b_num)
    return sum(2 ** i * d for i, d in enumerate(reversed(max_num)))


def nth_in_nonine_sequence(n):
    result = []
    while n:
        result.append(str(n % 9))
        n //= 9
    return int(''.join(reversed(result)) or '0')
