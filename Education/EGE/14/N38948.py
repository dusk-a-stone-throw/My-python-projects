a = set()
n = 4**36 + 3 * 4**20 + 4**15 + 2 * 4**7 + 49
s = str(hex(n)[2:])
for i in range(len(s)):
    a.add(s[i])
print(len(a))
