def algorithm(n):
    count = 0
    for i in range(n, n**2):
        if i % 2 == 1:
            count = count + 1
    return count

print(algorithm(100))