from random import randint

from timer import timer


def create_matrix(n, m):
    return [[(1, 0)[(j % 2) * (i % 2)] for j in range(m)] for i in range(n)]


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


def is_symmetric(matrix):
    result = ['no']
    if all(matrix[i] == matrix[~i] for i in range(len(matrix) // 2)):
        result.append('horizontal')
    if all(all(matrix[i][j] == matrix[i][~j] for j in range(len(matrix) // 2)) for i in range(len(matrix))):
        result.append('vertical')
    return (result[-1], 'both')[len(result) == 3]


def sum_diagonal_extremes(matrix):
    return max(matrix[i][i] for i in range(len(matrix))) + min(matrix[~i][i] for i in range(len(matrix)))


def can_match_by_rotation(A, B):
    if all(all(A[i][j] == B[i][j] for j in range(len(A))) for i in range(len(A))):
        return True
    if all(all(A[i][j] == B[j][~i] for j in range(len(A))) for i in range(len(A))):
        return True
    if all(all(A[i][j] == B[~i][~j] for j in range(len(A))) for i in range(len(A))):
        return True
    if all(all(A[i][j] == B[~j][i] for j in range(len(A))) for i in range(len(A))):
        return True
    return False


def create_matrix(n):
    return [[(j - i) % 3 for j in range(n)] for i in range(n)]


def create_matrix(n):
    return [[max(0, (2 * n + i - j + 1) * (j - i) // 2 + i + 1) for j in range(n)] for i in range(n)]


def rotate180(m):
    for i in range(len(m) // 2):
        for j in range(i, len(m) - i - 1):
            m[i][j], m[j][~i], m[~i][~j], m[~j][i] = m[~i][~j], m[~j][i], m[i][j], m[j][~i]


def rotate180_reverse(mx):
    [el.reverse() for el in mx]
    mx.reverse()


def create_matrix(n, m):
    return [[min(i, j, n - i - 1, m - j - 1) + 1 for j in range(m)] for i in range(n)]


def matrix_search(matrix, target):
    top = 0
    bottom = len(matrix) - 1
    while top < bottom:
        mid = top + (bottom - top) // 2
        if matrix[top][0] <= target <= matrix[top][-1]:
            break
        elif matrix[mid][0] > target:
            bottom = mid - 1
            top += 1
        elif matrix[mid][-1] < target:
            top = mid + 1
        else:
            top += 1
            bottom -= 1

    while top < len(matrix) and matrix[top][0] <= target <= matrix[top][-1]:
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[top][mid] == target:
                return True
            elif matrix[top][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        top += 1
    return False


def sum_shaded_area(matrix):
    n = len(matrix)
    return sum(matrix[i][j] for i in range(n) for j in range(abs(n // 2 - i), n - abs(n // 2 - i)))


def saddle_points(matrix):
    n = len(matrix)
    m = len(matrix[0])
    mins = [min(row) for row in matrix]
    maxes = [max(matrix[i][j] for i in range(n)) for j in range(m)]
    return sum(matrix[i][j] == mins[i] and matrix[i][j] == maxes[j] for i in range(n) for j in range(m))


def winner(scores):
    return -max((max(scores[i]), sum(scores[i]), -i) for i in range(len(scores)))[2]


def count_columns_with_max(matrix):
    count = 0
    max_elem = max((max(row) for row in matrix))
    for i in range(len(matrix)):
        if max_elem in (matrix[j][i] for j in range(len(matrix))):
            count += 1
    return count
