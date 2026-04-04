def cube_root(num):
    epsilon = 0.000001
    left = 0
    right = max(1, num)
    while right ** 3 - left ** 3 > epsilon:
        mid = (right + left) / 2
        if mid ** 3 < num:
            left = mid
        else:
            right = mid
    return left


# from math import log2
# def solve_equation(a):
#     f = lambda x: 2 ** x + x ** 0.5
#     left = 0
#     right = max(1, log2(a) + 1)
#     epsilon = 0.000001
#     while right - left > epsilon:
#         mid = (left + right) / 2
#         if f(mid) < a:
#             left = mid
#         else:
#             right = mid
#     return left

def solve_equation(a, b, c, d):
    f = lambda x: a * x ** 3 + b * x ** 2 + c * x + d
    m = max(abs(a), abs(b), abs(c), abs(d))
    left = - m ** 4
    right = - left
    epsilon = 0.0000001
    while right - left > epsilon:
        mid = (left + right) / 2
        m = f(mid)
        r = f(right)
        if m == 0:
            return mid
        if m < 0 <= r or r <= 0 < m:
            left = mid
        else:
            right = mid
    return left
