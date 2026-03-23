def fizz_buzz(n: int) -> tuple[int, int, int]:
    a = (n - 1) // 3
    b = (n - 1) // 5
    c = (n - 1) // 15
    return a - c, b - c, c


def calculate_sum(n: int) -> float:
    return 1 - 1 / n


def calculate_sum(n: int) -> float:
    return n * (n + 1) // 2


def max_consecutive_elements(s: str):
    max_l = 0
    l = 0
    last_c = None
    for c in s:
        if last_c == c:
            l += 1
        else:
            last_c = c
            max_l = max(max_l, l)
            l = 1
    return max(max_l, l)


def water_requirement(n: int) -> int:
    return n * (n + 1) + 1
