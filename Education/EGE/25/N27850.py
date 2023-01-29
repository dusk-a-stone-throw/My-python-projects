flag = False
k = 0
for i in range(245690, 245757):
    k += 1
    for j in range(2, round(i**0.5) + 1):
        if (i % j == 0):
            flag = True
            break
    if (flag):
        flag = False

    else:
        print(k, i)
