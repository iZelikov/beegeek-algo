def get_quadrant(p):
    if p[0] > 0:
        if p[1] > 0:
            return 1
        elif p[1] < 0:
            return 4
    elif p[0] < 0:
        if p[1] > 0:
            return 2
        elif p[1] < 0:
            return 3


def is_point_in_rectangle(p, rect):
    return rect[0][0] < p[0] < rect[1][0] and rect[0][1] < p[1] < rect[1][1]


def draw_graph(f):
    n = 9
    width = 3
    n = n + 1
    underline = f'{'+':>{width}}' + '-' * width * (n - 1) + ' > x'
    abscissas = ' ' * width + ''.join([f'{i:>{width}}' for i in range(1, n)])
    matrix = [[' '*width for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][0] = f'{(n - i):<{width-1}}|'
        if i > 0:
            y = f(i)
            if 1 <= y < n:
                matrix[n - y][i] = f'{"*":>{width}}'
    matrix[0][0] = 'y ^'
    [print(*line, sep='') for line in matrix]
    print(underline)
    print(abscissas)