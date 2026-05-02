def create_matrix(n, m):
    return [[j for j in range(m)] for _ in range(n)]


def create_matrix(n):
    return [[(0, 1)[i == j or i == (n - j - 1)] for j in range(n)] for i in range(n)]


def create_matrix(n):
    return [[(1 - (i == j), 2)[i > j] for j in range(n)] for i in range(n)]


def create_matrix(n):
    matrix = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j or i == n - j - 1:
                matrix[i].append(0)
            elif i < j < n - i - 1:
                matrix[i].append(1)
            elif i < j:
                matrix[i].append(2)
            elif j < i < n - j - 1:
                matrix[i].append(4)
            else:
                matrix[i].append(3)

    return matrix


def create_matrix(n):
    matrix = [[1] for _ in range(n)]
    matrix[0] = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            matrix[i].append(matrix[i - 1][j] + matrix[i][j - 1])
    return matrix


def create_matrix(n, m, k):
    return [[(0, 1)[i + j == k] for j in range(m)] for i in range(n)]


def create_matrix(n, m):
    return [[i + 1 + j * n for j in range(m)] for i in range(n)]


def create_matrix(n, m):
    return [[n * m - i * m - j for j in range(m)] for i in range(n)]


def create_matrix(n, m):
    return [[i + j + 1 for j in range(m)] for i in range(n)]


def create_matrix(n):
    return [[abs(i - j) + 1 for j in range(n)] for i in range(n)]


def create_matrix(n, m):
    return [[(n - i) + j * n for j in range(m)] for i in range(n)]


def create_matrix(n, m):
    return [[(i + 1, n - i)[j % 2] + j * n for j in range(m)] for i in range(n)]


def create_matrix(n):
    return [[(0, 1)[abs(i + j + 1 - n) <= 1] for j in range(n)] for i in range(n)]


def create_matrix(n):
    return [[(1, 0)[j % 2 and i >= j or i % 2 and j >= i] for j in range(n)] for i in range(n)]


def create_matrix(n):
    return [[1 - (j % 2) ^ (i % 2) for j in range(n)] for i in range(n)]


def create_matrix(n):
    return [[min(j + 1, n - i) for j in range(n)] for i in range(n)]


def create_matrix(n):
    return [[min(i + 1, j + 1, n - i, n - j) % 2 for j in range(n)] for i in range(n)]


def create_matrix(n, m):
    d_x = -1
    d_y = 1
    x = y = 0
    matrix = [[0] * m for _ in range(n)]
    for i in range(1, n * m + 1):
        matrix[y][x] = i

        if d_x == 0:
            d_x = (-1, 1)[x == 0]
            d_y = (1, -1)[x == 0]

        if d_y == 0:
            d_x = (1, -1)[y == 0]
            d_y = (-1, 1)[y == 0]

        if x + d_x < 0 or x + d_x >= m:
            d_x = 0
            d_y = 1

        if y + d_y < 0 or y + d_y >= n:
            d_x = 1
            d_y = 0

        x += d_x
        y += d_y

    return matrix


def create_matrix(n, m):
    x = -1
    y = 0
    d_x = 1
    d_y = 1
    i = 1
    length = n * m + 1
    matrix = [[0] * m for _ in range(n)]
    while i < length:
        for _ in range(m):
            x += d_x
            matrix[y][x] = i
            i += 1
        n -= 1
        for _ in range(n):
            y += d_y
            matrix[y][x] = i
            i += 1
        m -= 1
        d_x = -d_x
        d_y = -d_y
    return matrix
