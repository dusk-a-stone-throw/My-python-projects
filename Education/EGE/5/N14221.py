arr = []
for i in range(100, 1000):
    s = str(i)
    a = str(int(s[0]) + int(s[1]))
    b = str(int(s[1]) + int(s[2]))
    c = 0
    if (a >= b):
        c = int(a + b)
    else:
        c = int(b + a)
    if (c == 714):
        arr.append(i)
print(min(arr))
