def quadratic_values(a, b, c, start=0, step=1):
    return [(x, a * x ** 2 + b * x + c) for x in range(start, start + step * 10, step)]


def solve(a, b, c):
    if a == 0:
        if b:
            return {-c / b}
        else:
            return set()

    d = b ** 2 - 4 * a * c
    if d < 0:
        return set()
    elif d == 0:
        return {-b / (2 * a)}
    else:
        return {(-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)}


def str_coef(a: int, x: bool = True):
    if a == 1:
        return ' + ' if x else ' + 1'
    elif a == -1:
        return ' - ' if x else ' - 1'
    elif a > 0:
        return f' + {a}'
    else:
        return f' - {abs(a)}'


def quadratic(x1, x2):
    b = -(x1 + x2)
    c = x1 * x2
    if b and c:
        return f'x^2{str_coef(b)}x{str_coef(c, x=False)} = 0'
    elif b:
        return f'x^2{str_coef(b)}x = 0'
    elif c:
        return f'x^2{str_coef(c, x=False)} = 0'
    else:
        return 'x^2 = 0'


def quadratic_intersections(a1, b1, c1, a2, b2, c2):
    return set(map(lambda x: (x, a1 * x ** 2 + b1 * x + c1), solve(a1 - a2, b1 - b2, c1 - c2)))
