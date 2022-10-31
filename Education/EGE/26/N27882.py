f = open("27882.txt")
a = f.readlines()
s = 1405
n = 5560
a.pop(0)
a = list(map(int, a))
a.sort()
maxUsers = 0
usedSpace = 0
i = 0
b = []
while True:
    if (usedSpace + a[i] <= s and i < n):
        usedSpace += a[i]
        b.append(a[i])
        i += 1
    else:
        print(usedSpace)
        print(i)
        break
j = 1
freeSpace = s - usedSpace + b[len(b) - j]
print(freeSpace)
while True:
    if freeSpace in a:
        print(freeSpace)
        break
    else:
        j += 1
        freeSpace += b[len(b) - j]
