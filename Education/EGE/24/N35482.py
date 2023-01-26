from collections import Counter

f = open("35482.txt")
a = f.readlines()
b = []
d = []
for i in range(len(a)):
    b.append(a[i].count("G"))
f = Counter(str(a[b.index(min(b))]))
print(f.most_common()[0][0])
g = {"1": "a"}
print(g[0])
