f = open("47221.txt")
a = list(map(int, f.readlines()))
maxElem = max(i for i in a if i % 10 == 3)
maxSum = -(10 ** 10)
k = 0
for i in range(len(a) - 1):
    if ((abs(a[i]) % 10 == 3) != (abs(a[i + 1]) % 10 == 3)) and (
        a[i] ** 2 + a[i + 1] ** 2) >= maxElem ** 2:
        maxSum = max(maxSum, a[i] ** 2 + a[i + 1] ** 2)
        k += 1
print(k, maxSum)
