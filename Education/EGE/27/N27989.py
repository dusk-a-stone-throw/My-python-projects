f = open("27989_B.txt")
n = int(f.readline())
from math import comb
# a product of two numbers a*b is divisiable by x when ((a % x) * (b % x)) % x == 0
d13 = 0  # nums that == 13 % 26
d2 = 0  # nums that == 2 % 26
d26 = 0
others = 0
for s in f:
    a = int(s)
    if a % 26 == 0:
        d26 += 1
    elif a % 13 == 0:
        d13 += 1
    elif a % 2 == 0:
        d2 += 1
    else:
        others += 1
print(d26 * (n - d26) + d2 * d13 + comb(d26, 2))
