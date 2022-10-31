import math

f = open("33105.txt")
a = list(map(int, f.readlines()))
n = a[0]
a.pop(0)
sum = 0
b = []
for i in range(len(a)):
    if a[i] <= 100:
        sum += a[i]
for i in range(len(a)):
    if a[i] > 100:
        b.append(a[i])
b.sort()
items = []
for i in range(len(b)):
    if i < len(b) // 2:
        sum += b[i] * 0.70
        items.append(b[i])
    else:
        sum += b[i]
print(math.ceil(sum), max(items))
