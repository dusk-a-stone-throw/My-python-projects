def f(n):
    if (n == 0):
        return 0
    if (n > 0 and n % 3 == 0):
        return f(n / 3)
    if (n % 3 > 0):
        return n % 3 + f(n - (n % 3))


for i in range(1000):
    if (f(i) == 11):
        print(i)
        break
