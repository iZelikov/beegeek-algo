# def calculate_sum(n) -> int:
#     return ((n**2 + 1) * n**2) // 2

# def calculate_sum(n) -> int:
#     return n ** 2

# def calculate_sum(n) -> int:
#     return ((n + 1) * n // 2) ** 2


def get_exam_position(n, k) -> int:
    return k // 2 + 1 + (n // 2 + n % 2 - 1) * (1 - k % 2)


def count_solutions(n) -> int:
    counter = 0
    for z in range(1, n - 4):
        for y in range(1, (n - 3 - z) // 2 + 1):
            x = max(1, (n - z - 2 * y) // 3)
            if 3 * x + 2 * y + z == n:
                counter += 1
    return counter


def area_of_tree(n: int) -> int:
    return n ** 2 + 3 * n + 1


def diff_even_odd(a: int, b: int):
    even_start = a + a % 2
    even_end = b - b % 2
    odd_start = a + (1 - a % 2)
    odd_end = b - (1 - b % 2)
    even_sum = (even_start + even_end) * ((even_end - even_start) // 2 + 1) // 2
    odd_sum = (odd_start + odd_end) * ((odd_end - odd_start) // 2 + 1) // 2
    return even_sum - odd_sum


def calculate_product(n: int) -> float:
    return 1 / n


# def calculate_sum(n: int) -> int:
#     last_even = n - n % 2
#     return - (3 + (2 * last_even - 1)) * last_even // 4 + n ** 2 * (n % 2)


def sold_out(n: int, m: int) -> int:
    return max(2 * m - 2 * n + 2, 1)


def calculate_sum(n: int) -> int:
    return 2 ** (n + 1) - 1


def number_of_handshakes(n: int) -> int:
    return n * (n - 1) // 2


def count_friends(k: int) -> int:
    return int((1 + (1 + 8 * k) ** 0.5) // 2)
