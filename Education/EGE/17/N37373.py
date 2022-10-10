f = open("37373.txt")
a = []
a = list(map(int, f.readlines()))
a.sort()
k = 0
maxI = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if ((a[i] - a[j]) % 36 == 0 and ((a[i] % 13 == 0) or a[j] % 13 == 0)):
            k += 1
            maxI = max(maxI, abs(a[i] - a[j]))
        print(i, j)
print(k, maxI)
