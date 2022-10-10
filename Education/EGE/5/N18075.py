for i in range(1000):
    a = bin(i)[2:]
    s = str(a)
    j = 0
    for i in range(len(s)):
        j += int(s[i])
    s = s + str(j % 2)
    j = 0
    for i in range(len(s)):
        j += int(s[i])
    s = s + str(j % 2)
    if (int(s, 2) > 123):
        print(int(s, 2))
        break
