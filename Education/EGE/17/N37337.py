f = open("37337.txt")
a = list(map(int, f.readlines()))
a.sort()
maxSum = 0
k = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if ((a[i] % 160) != (a[j] % 160)) and (a[i] % 7 == 0 or a[j] % 7 == 0):
            maxSum = max(maxSum, i + j)
            k += 1
print(k, maxSum)
