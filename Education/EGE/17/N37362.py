f = open("37362.txt")
a = list(map(int, f.readlines()))
a.sort()
b = []
c = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if ((a[i] + a[j]) % 80 == 0) and ((a[i] % 50 == 0) or
                                          (a[j] % 50 == 0)):
            c += 1
            b.append(a[i] + a[j])
print(c, max(b))
