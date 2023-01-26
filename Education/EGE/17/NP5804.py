import re

f = open("P5804.txt")
a = list(map(int, f.readlines()))
pattern = re.compile("11.*6.*")


def f(number):
    s = 1
    st = str(number)
    for i in range(len(st)):
        if int(st[i]) % 2 == 0:
            s *= int(st[i])
    return s if s != 1 else 2 * 10**9 + 1


maxP = 0
c = 0
for i in range(0, len(a) - 2):
    tmp = (f(a[i]) * f(a[i + 1]) * f(a[i + 2]))
    if (tmp <= 2 * 10**9) and pattern.fullmatch(str(tmp)):
        maxP = max(maxP, tmp)
        c += 1
print(c, maxP)
