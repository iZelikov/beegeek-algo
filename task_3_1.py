from math import log


def is_power_of_four(n: int) -> bool:
    return log(n, 4).is_integer()


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


def intersections(a, b, c, k, m):
    roots = solve(a, b-k, c-m)
    result = set(map(lambda x: (x, k * x + m), roots))
    return result

def optimal_value(nums: list[int]) -> float:
    return sum(nums) / len(nums)