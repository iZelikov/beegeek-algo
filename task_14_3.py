def hex_digit(num):
    extra = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    return extra.get(num, num)


def to_decimal(str_num, base):
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d_dict = {v: i for i, v in enumerate(digits)}
    result = 0
    if len(str_num) > 1:
        for i, d in enumerate(reversed(str_num)):
            result += base ** i * d_dict[d]
    elif d_dict[str_num] < base:
        result = d_dict[str_num]
    else:
        result = -1
    return result


def find_number_system(str_num, num):
    for base in range(2, 37):
        if to_decimal(str_num, base) == num:
            return base
