def linear_coefficients(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0]), (p1[1] * p2[0] - p1[0] * p2[1]) / (p2[0] - p1[0])


def on_one_line(p1, p2, p3):
    return linear_coefficients(p1, p2) == linear_coefficients(p1, p3)


def equation_of_line(values):
    lines = [on_one_line((i, values[i]), (i + 1, values[i + 1]), (i + 2, values[i + 2])) for i in range(3)]
    if all(lines):
        k, b = linear_coefficients((0, values[0]), (1, values[1]))
        if k == 1:
            str_x = 'x'
        elif k == -1:
            str_x = '-x'
        else:
            str_x = f'{int(k)}x'
        if k and b:
            return f'y = {str_x} {'+' if b > 0 else '-'} {abs(int(b))}'
        elif k:
            return f'y = {str_x}'
        elif b:
            return f'y = {int(b)}'
        else:
            return 'y = 0'
    else:
        return None
