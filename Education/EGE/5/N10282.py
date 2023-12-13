for i in range(10000, 100000):
    s = str(i)
    k1 = int(s[0]) + int(s[2]) + int(s[4])
    k2 = int(s[1]) + int(s[3])
    if int("".join(map(str, sorted([k1, k2])))) == 723:
        print(i)
        break
