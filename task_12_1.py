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
    pass