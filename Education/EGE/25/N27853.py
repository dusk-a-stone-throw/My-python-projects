for i in range(312614, 312652):
    a = []
    k = 1
    for j in range(1, i // 2 + 1):
        if (i % j == 0):
            k += 1
            a.append(j)
        if (k > 6):
            break
    if (k == 6):
        print(a, i)
    a = 0
