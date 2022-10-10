for a in range(1000):
    g = True
    for x in range(1000):
        for y in range(1000):
            if (not ((5 * x + 3 * y != 60) or ((a > x) and (a > y)))):
                print(a, x, y)
                g = False
                break
    if (g):
        print(a)
        break
