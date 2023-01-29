def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)


print(f(2, 14) * f(14, 28))
