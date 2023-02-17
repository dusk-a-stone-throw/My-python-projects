f = open("P5164.txt")
a = [int(i) for i in f.readlines()]
max_197 = max(i for i in a if i % 197 == 0)
m = 0
k = 0
for i in range(len(a) - 1):
    if any(a[i] == int(x) * 197 for x in str(a[i])) != any(
            a[i + 1] == int(x) * 197
            for x in str(a[i + 1])) and (a[i] + a[i + 1] < max_197):
        k += 1
        m = max(m, a[i] + a[i + 1])
print(k, m)
