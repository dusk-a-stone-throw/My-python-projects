nums = []
res = []
for i in range(0, 10):
    for j in range(0, 10):
        tmp1 = "12345" + str(i) + "7" + str(j) + "8"
        tmp = int(tmp1)
        if (int(tmp) % 23 == 0):
            print(tmp)
            print(tmp % 23)
            nums.append(tmp)
            res.append(tmp / 23)
print(nums)
print(res)
