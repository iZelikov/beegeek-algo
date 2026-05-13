from collections import Counter
from random import randint

from timer import timer


def nearest_divisible_by_ten(n):
    return (round(n, -1), n + 5)[n % 10 == 5]


def is_divisible_by_nine(str_num):
    if len(str_num) == 1:
        return str_num in ('0', '9')
    else:
        return is_divisible_by_nine(str(sum(map(int, str_num))))


def is_divisible_by_forty(str_num):
    return str_num[-1] in ('0', '5') and int(str_num[-3:]) & 7 == 0


def is_divisible_by_thirty_three(str_num):
    return sum(map(int, str_num)) % 3 == 0 and (sum(map(int, str_num[::2])) - sum(map(int, str_num[1::2]))) % 11 == 0


def change_one_digit(list_num):
    mod = sum(list_num) % 3
    plus = 3 - mod
    for i in range(len(list_num)):
        extra = 9 - list_num[i]
        if extra >= plus:
            list_num[i] += plus + (extra - plus) // 3 * 3
            return list_num

    list_num[-1] -= (3, mod)[mod > 0]
    return list_num


# @timer
def create_number(digits: list[int]):
    def result(count_):
        return int(''.join(str(d) * count_d[d] for d in range(9, -1, -1)))

    count_d = Counter(digits)
    mod_3 = sum(d * count for d, count in count_d.items())  % 3
    if count_d[0] == 0:
        return -1
    elif mod_3 == 0:
        return result(count_d)
    else:
        for d in sorted(count_d):
            if d % 3 == mod_3:
                count_d[d] -= 1
                return result(count_d)
        for d, count in sorted(count_d.items()):
            if count > 1 and 2 * d % 3 == mod_3:
                count_d[d] -= 2
                return result(count_d)
        return -1


def remove(count, mod, k):
    removed = 0
    for d in range(mod, 10, 3):
        while count[d] > 0 and removed < k:
            count[d] -= 1
            removed += 1
        if removed == k:
            return True
    return False


@timer
def create_number_2(digits):
    count = [0] * 10
    total = 0
    for d in digits:
        count[d] += 1
        total += d

    if count[0] == 0:
        return -1

    r = total % 3
    if r == 1:
        if not (remove(count, 1, 1) or remove(count, 2, 2)):
            return -1
    elif r == 2:
        if not (remove(count, 2, 1) or remove(count, 1, 2)):
            return -1

    result = ''.join(str(d) * count[d] for d in range(9, -1, -1))
    return "0" if not result.strip('0') else result


n = 1000
data = [randint(0, 9) for _ in range(n)]
data2 = data.copy()
create_number(data)
create_number_2(data2)
