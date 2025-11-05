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
    matrix = [['   ' for _ in range(n)] for _ in range(n)]
    for x in range(1, n+1):
        y = f(x)
        if 1 <= y <= n:
            print(x, y)
            matrix[y][x] = '  *'

    print(*matrix, sep='\n')

draw_graph(lambda x: x)