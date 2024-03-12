s = list(map(int, open("P4310.txt").readlines()))
k = 0
m = 0
for i in s:
    if i % 3 == 0 and i % 7 != 0 and i % 17 != 0 and i % 19 != 0 and i % 27 != 0:
        k += 1
        m = max(m, i)
print(k, m)
