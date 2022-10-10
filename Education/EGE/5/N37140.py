a = []
for i in range(1, 100000):
    b = bin(i)
    s = str(b)
    s = s.replace("0b", "")
    if (i % 2 == 0):
        s = "1" + s + "0"
    else:
        s = "11" + s + "11"
    if (int(s, 2) > 52):
        a.append(int(s, 2))
print(min(a))
