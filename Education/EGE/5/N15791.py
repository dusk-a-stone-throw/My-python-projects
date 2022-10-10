for i in range(200):
    n = bin(i)
    tmp = str(n)
    tmp = tmp.replace("0b", "")
    for k in range(2):
        s = 0
        for j in range(len(tmp)):
            s += int(tmp[j])
        tmp += (str(s % 2))
    print((int(tmp, 2)))
