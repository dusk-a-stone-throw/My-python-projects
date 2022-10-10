for x in range(0, 15):
    s = str(x)
    a = "123" + str(int(s, 15)) + "5"
    b = "1" + str(int(s, 15)) + "233"
    c = int(int(a, 15) + int(b, 15))
    if (int(str(c), 10) % 14 == 0):
        print(int(str(c), 10) / 14)
        break
