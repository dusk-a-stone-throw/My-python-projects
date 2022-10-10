a = 36**8 + 6**20 - 12
s = ""
while (a > 0):
    s = str((a % 6)) + s
    a = a // 6
print(s.count("0"))
