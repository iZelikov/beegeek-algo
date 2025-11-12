def mid_num(a, b, c):
    return a + b + c - max(a, b, c) - min(a, b, c)


def swap_digits(n):
    return n % 10 * 100 + n // 10 % 10 * 10 + n // 100


def max_guests(n, m):
    return (n - 1) * m * 3


def training_time(n, m, s, b):
    t = n * (m * 60 + s) + (n - 1) * b
    return t // 60, t % 60


def time_zone(h, a, b):
    return (h - a + b) % 24


def drop_one_and_five(n:int):
    result = 0
    i = 0
    while n:
        d = n % 10
        n = n // 10
        if d == 1 or d == 5:
            continue
        else:
            result += d * 10 ** i
            i += 1
    return result

def snake(n:int):
    for i in range(n):
        print(['*' * n, '*'.rjust(n), '*' * n, '*'][i % 4])
