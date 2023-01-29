f = open("28129_B.txt")
n = int(f.readline())
m = -10000
pair = [0, 0]
rems7 = {
}  # keep max numbers that % 7 == 0 and their remainders of division by 160 (from 0 to 159)
rems = {}  # all the same, but numbers that % 7 != 0
for i in range(0, 160):
    rems7[i] = 0
    rems[i] = 0
for s in f:
    a = int(s)
    if (a % 7 == 0):
        if rems7[a % 160] < a: rems7[a % 160] = a
    else:
        if rems[a % 160] < a: rems[a % 160] = a
for i in range(160):
    tmp = list(rems.values())
    tmp = tmp[:i] + tmp[i + 1:]
    if (rems7[i] + max(tmp) > m) and rems7[i] != 0:
        pair = sorted([rems7[i],
                       max(tmp)])  # according the task, keep ascending
    m = max(m, rems7[i] + max(tmp))
print(pair)
