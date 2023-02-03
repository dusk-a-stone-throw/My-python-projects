from math import comb

f = open("27990_B.txt")
n = int(f.readline())
# 62 = 31 * 2
a62 = 0
a31 = 0
a2 = 0
for i in f:
    i = int(i)
    if i % 62 == 0:
        a62 += 1
    elif i % 31 == 0:
        a31 += 1
    elif i % 2 == 0:
        a2 += 1
print(a31 * a2 + a62 * (n - a62) + comb(a62, 2))
