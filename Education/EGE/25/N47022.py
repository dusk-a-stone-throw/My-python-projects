i = 300 * 10**6 + 1
c = 0
while c < 5:
    k = 0
    for j in range((i - 1) // 2 + 1, 1, -1):
        print(i, j)
        if (i % j == 0):
            k += 1
            input()
        if (k == 5):
            print(j)
            c += 1
            break
    i -= 1
