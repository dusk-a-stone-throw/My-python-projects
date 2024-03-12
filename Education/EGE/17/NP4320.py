s = list(map(int, open("P4320.txt").readlines()))
k = 0
m = 10000000
for i in s:
    if (i % 10 == 2 or i % 10 == 7) and i % 3 == 0 and i % 11 == 0:
        k += 1
        m = min(m, i)
print(k, m)
