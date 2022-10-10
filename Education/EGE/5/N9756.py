for i in range(100, 1000):
    t = str(i)
    a = str(int(t[0]) * int(t[1]))
    b = str(int(t[1]) * int(t[2]))
    c = a + b
    if (int(c) == 621):
        print(i)
        break
