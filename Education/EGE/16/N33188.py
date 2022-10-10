def f(a):
    if (a == 0):
        return 0
    if (a % 3 == 0 and a > 0):
        return a + f(a - 3)
    if (a % 3 > 0):
        return a + f(a - (a % 3))


print(f(22))
