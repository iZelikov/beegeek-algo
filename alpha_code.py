def f(x):
    return 99*x**3 - 300* x**2 - 30000*x - 1000000


left, right = 0, 10**10
epsilon = 0.000001
i=0
while right - left > epsilon:
    i+=1
    middle = (left + right) / 2

    if f(middle) * f(right) < 0:
        left = middle
    else:
        right = middle

print(i)
print(left)
print(right)
