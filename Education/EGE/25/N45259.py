nums = []
res = []
for i in range(0, 10):
    for j in range(0, 10):
        tmp = int("12345" + str(i) + "7" + str(j) + "8")
        if (int(tmp) % 23 == 0):
            print(tmp, tmp // 23)
