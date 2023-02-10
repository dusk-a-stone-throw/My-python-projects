f = open("35916_B.txt")
n = int(f.readline())
a = list(map(int, f.readlines()))
# (a + b + c) % 3 ==0 if:
# 1) a % 3 == b % 3 == c % 3 == 0
# 2) a % 3 == b % 3 == c % 3 == 1
# 3) a % 3 == b % 3 == c % 3 == 2
# 4) a % 3 == 2, b % 3 == 1, c % 3 == 0
r0 = sorted(i for i in a if i % 3 == 0)[:3]
r1 = sorted(i for i in a if i % 3 == 1)[:3]
r2 = sorted(i for i in a if i % 3 == 2)[:3]
sum0 = sum(r0)  # 1)
sum1 = sum(r1)  # 2)
sum2 = sum(r2)  # 3)
# For sum3 you may take the first elements cuz lists are sorted
sum3 = r0[0] + r1[0] + r2[0]  # 4)
print(min(sum0, sum1, sum2, sum3))
