import itertools
from itertools import dropwhile, zip_longest, starmap


def polynomial_sum(p1, p2):
    return tuple(dropwhile(lambda x: x == 0,
                           tuple(starmap(lambda x, y: x + y, zip_longest(p1[::-1], p2[::-1], fillvalue=0)))[::-1]))


def str_coef(a: int):
    if a == 1:
        return '+'
    elif a == -1:
        return '-'
    elif a == 0:
        return ''
    elif a > 0:
        return f'+{a}'
    else:
        return f'-{abs(a)}'


def str_x(power: int):
    if power == 0:
        return ''
    elif power == 1:
        return 'x'
    else:
        return f'x^{power}'


def polynomial(p):
    polinom = [str_coef(a) + str_x(len(p) - i - 1) for i, a in enumerate(p) if str_coef(a)]
    polinom[-1] = '+1' if polinom[-1] == '+' else '-1' if polinom[-1] == '-' else polinom[-1]
    return ''.join(polinom).lstrip('+')


def polynomial_creator(p: tuple[int]):
    return lambda x: sum(map(lambda i: i[1] * x ** (len(p) - i[0] - 1), enumerate(p)), 0)


def polynomial_product(p1, p2):
    result = {}
    for i, v1 in enumerate(p1[::-1]):
        for j, v2 in enumerate(p2[::-1]):
            result[i + j] = result.get(i + j, 0) + v1 * v2
    return tuple(v for i, v in sorted(result.items(), reverse=True))
