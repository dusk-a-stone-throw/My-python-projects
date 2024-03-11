s = open("P5878.txt").readline()
m = [0] * len(s)
for i in range(2, len(s)):
    if s[i] == s[i - 1] == s[i - 2]:
        m[i] = m[i - 3] + 3
print(max(m))
