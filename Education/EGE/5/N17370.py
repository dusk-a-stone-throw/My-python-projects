a = set()
for i in range(100, 3001):
    b = bin(i)[3:]
    a.add((int(b, 2)) - i)
print(len(a))
