for i in range(1, 100):
    a = i
    s = ""
    while a > 0:
        s = str(a % 3) + s
        a = a // 3
    s += str(i % 3)
    if int(s, 3) > 99:
        print(int(s, 3))
        break
