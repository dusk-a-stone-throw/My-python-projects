f = open("35482.txt")
a = f.readlines()
b = []
c = []
d = []
for i in range(len(a)):
    b.append(a[i].count("G"))
    c.append(a[i])
f = str(a[b.index(min(b))])
for i in f:
    d.append(f.count(i))
print(f[d.index(max(d))])
