def count_even_digits(n):
    count = 0
    while n > 0:
        count += (n % 2 == 0)
        n //= 10
    return count


def create_number(digits):
    return sum(10 ** i * d for i, d in enumerate(reversed(digits)))


def filtered_reverse(n):
    result = 0
    while n > 0:
        d = n % 10
        result = (result, result * 10 + n % 10)[d not in (6, 9)]
        n //= 10
    return result


def expanded_form(n):
    digits = list(str(n))
    for i, v in enumerate(reversed(digits[:-2]), 2):
        digits[~i] = f'{v}*10^{i}'
    if len(digits) >= 2:
        digits[-2] += '*10'
    return ' + '.join(digits)


def digital_root(n):
    return (9, n % 9)[n % 9 > 0]
