f = open("27891_B.txt")
a = list(map(int, f.readlines()))
a.pop(0)
b = []  # % 14 == 0
c = []  # % 7 == 0
d = []  # % 2 == 0
e = []  # others
for i in range(len(a)):
    if (a[i] % 14 == 0):
        b.append(a[i])
    if (a[i] % 7 == 0):
        c.append(a[i])
    if (a[i] % 2 == 0):
        d.append(a[i])
    else:
        e.append(a[i])
print(max((max(b) * max(max(c), max(d), max(e))), (max(c) * max(d))))
