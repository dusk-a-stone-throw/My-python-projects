f = open("37344.txt")
a = [int(i) for i in f.readlines()]
m = 0
k = 0
for i in range(0, len(a) - 1):
    for j in range(i + 1, len(a)):
        if (a[i] * a[j]) % 10 == 0:
            k += 1
            m = max(m, a[i] + a[j])
print(k, m)
