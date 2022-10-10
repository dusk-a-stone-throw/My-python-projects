for i in range(100):
    b = bin(i)[2:]
    s = str(b)
    if (i % 2 == 0):
        s = s + "00"
    else:
        s = s + "11"
    b = int(s, 2)
    if (b > 115):
        print(i)
        break
