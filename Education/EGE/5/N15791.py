for i in range(200):
    n = bin(i)
    tmp = str(n)[2:]
    for k in range(2):
        s = 0
        for j in range(len(tmp)):
            s += int(tmp[j])
        tmp += (str(s % 2))
    if int(tmp, 2) > 97:
        print((int(tmp, 2)))
        break
