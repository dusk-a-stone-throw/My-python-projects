flag = False
k = 0
for i in range(245690, 245757):
    k += 1
    for j in range(3, i):
        if (i % j == 0):
            flag = True
            break
    if (flag):
        flag = False

    else:
        print(k, i)
