a = []
for i in range(1000):
    b = bin(i)[2:]
    s = str(b)
    if (s.count("1") > s.count("0")):
        s += "1"
    else:
        s += "0"
    b = int(s, 2)
    if (b > 100):
        a.append(b)
print(min(a))
