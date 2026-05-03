from itertools import pairwise


def is_special(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j or i == len(matrix) + ~j:
                if not matrix[i][j]:
                    return False
            else:
                if matrix[i][j]:
                    return False
    return True


def winner(game_area):
    l = len(game_area)
    for i in range(l):
        if game_area[i][0] != '-' and all(game_area[i][j] == game_area[i][0] for j in range(1, l)):
            return game_area[i][0]

        if game_area[0][i] != '-' and all(game_area[j][i] == game_area[0][i] for j in range(1, l)):
            return game_area[0][i]

    if game_area[0][0] != '-' and all(game_area[i][i] == game_area[0][0] for i in range(1, l)):
        return game_area[0][0]

    if game_area[0][-1] != '-' and all(game_area[i][~i] == game_area[0][-1] for i in range(1, l)):
        return game_area[0][-1]

    return 'Draw'


def sum_middle_row_and_column(matrix):
    n = len(matrix)
    return sum(matrix[n // 2][i] for i in range(n)) + sum(matrix[i][n // 2] for i in range(n)) - matrix[n // 2][n // 2]


def count_special_positions(matrix: list[list[int]]):
    result_j = {}
    result_i = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                result_j[j] = result_j.get(j, 0) + 1
                result_i[i] = result_i.get(i, 0) + 1
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                count += result_j[j] == 1 and result_i[i] == 1
    return count


def reshape(matrix, row, col):
    return [[matrix[(j + col * i) // len(matrix[0])][(j + col * i) % len(matrix[0])] for j in range(col)] for i in
            range(row)]


def count_sorted_rows(matrix):
    return sum(all(b > a for a, b in pairwise(row)) or all(a > b for a, b in pairwise(row)) for row in matrix)


def rotate90(m):
    for i in range(len(m) // 2):
        for j in range(i, len(m) - i - 1):
            m[i][j], m[j][~i], m[~i][~j], m[~j][i] = m[~j][i], m[i][j], m[j][~i], m[~i][~j]


def fill_ones(matrix):
    rows = [0] * len(matrix)
    cols = [0] * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                rows[i] = 1
                cols[j] = 1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if rows[i] or cols[j]:
                matrix[i][j] = 1


def has_common_element_in_rows(matrix):
    numbers = set(matrix[0])
    for i in range(1, len(matrix)):
        numbers &= set(matrix[i])
    return bool(numbers)


def count_zeros(matrix):
    i = len(matrix) - 1
    j = 0
    count = 0
    while j < len(matrix) and i >= 0:
        if matrix[i][j] == 0:
            j += 1
        else:
            i -= 1
            count += j
    return count + (0, j * (i + 1))[i >= 0]


def row_with_max_ones(matrix):
    i = 0
    j = len(matrix[0]) - 1
    max_row_index = -1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] == 1:
            max_row_index = i
            j -= 1
        else:
            i += 1
    return max_row_index


def sort_each_diagonal(matrix):
    for i in range(-len(matrix) + 2, len(matrix) - 1):
        x = (0, i)[i > 0]
        y = (0, -i)[i < 0]
        diag = sorted(matrix[x + n][y + n] for n in range(len(matrix) - abs(i)))
        for n in range(len(matrix) - abs(i)):
            matrix[x + n][y + n] = diag[n]


def shift_by_one_in_spiral_order(matrix):
    x = -1
    y = 0
    d_x = 1
    d_y = 1
    i = 0
    n = len(matrix)
    m = len(matrix[0])
    length = n * m
    current = None
    while i < length:
        for _ in range(m):
            x += d_x
            matrix[y][x], current = current, matrix[y][x]
            i += 1
        n -= 1
        for _ in range(n):
            y += d_y
            matrix[y][x], current = current, matrix[y][x]
            i += 1
        m -= 1
        d_x = -d_x
        d_y = -d_y
    matrix[0][0] = current
