def diagonal_sum(matrix):
    return sum(matrix[i][i] + matrix[~i][i] for i in range(len(matrix))) - matrix[len(matrix) // 2][
        len(matrix) // 2] * (len(matrix) % 2)


def is_symmetric(matrix):
    for i in range(len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def sum_shaded_area(matrix):
    return sum(
        matrix[i][j] + matrix[~i][~j] for i in range(len(matrix) // 2) for j in range(i + 1, len(matrix) - i - 1))


def max_on_main_diagonal(matrix):
    return max(matrix[i][i] for i in range(len(matrix)))


def is_toeplitz_matrix(matrix):
    for i in range(len(matrix) - 1):
        if any(matrix[j][i + j] != matrix[0][i] for j in range(len(matrix) - i)):
            return False
        if any(matrix[i + j][j] != matrix[i][0] for j in range(len(matrix) - i)):
            return False
    return True


def print_matrix_diagonally(matrix):
    for i in range(-len(matrix) + 1, len(matrix)):
        start = i + len(matrix) - 1
        shift = ((i + len(matrix)) // len(matrix)) * (i % len(matrix))
        length = len(matrix) - abs(i)
        print(*(matrix[start - shift - j][j + shift] for j in range(length)))


def min_below_secondary_diagonal(matrix):
    return min(matrix[i][~j] for i in range(1, len(matrix)) for j in range(i))


def is_magic_square(matrix):
    s = (len(matrix) ** 2 + 1) * len(matrix) // 2
    if any(sum(matrix[i][j] for j in range(len(matrix))) != s for i in range(len(matrix))):
        return False
    if any(sum(matrix[j][i] for j in range(len(matrix))) != s for i in range(len(matrix))):
        return False
    if sum(matrix[i][i] for i in range(len(matrix))) != s:
        return False
    if sum(matrix[i][~i] for i in range(len(matrix))) != s:
        return False
    return True


def is_diagonally_dominant(matrix):
    return all(2 * abs(matrix[i][i]) >= sum(map(abs, matrix[i])) for i in range(len(matrix)))


def sum_edge_elements(matrix):
    return sum(matrix[0]) + (0, sum(matrix[len(matrix) - 1]))[len(matrix) > 1] + sum(
        matrix[i][0] + matrix[i][len(matrix) - 1] for i in range(1, len(matrix) - 1))


def print_matrix_with_reversed_rows(matrix):
    for row in matrix:
        for i in reversed(row):
            print(i, end=' ')
        print()


def modify_by_average(matrix):
    avg = sum(sum(row) for row in matrix) / (len(matrix) * len(matrix[0]))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = (0, 1)[matrix[i][j] >= avg]


def row_with_min_sum(matrix):
    return -min((sum(row), -i) for i, row in enumerate(matrix))[1]

def count_columns(matrix, target):
    count = 0
    for j in range(len(matrix)):
        for i in range(len(matrix)):
            if matrix[i][j] == target:
                count+=1
                break
    return count
