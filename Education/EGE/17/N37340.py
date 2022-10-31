f = open("37340.txt")
a = list(map(int, f.readlines()))
count = 0
m = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if ((a[i] - a[j]) % 2 == 0) and (a[i] % 31 == 0 or a[j] % 31 == 0):
            count += 1
            m = max(m, a[i] + a[j])
print(count, m)
