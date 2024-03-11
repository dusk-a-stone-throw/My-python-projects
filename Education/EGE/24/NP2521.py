s = open("P2521.txt").readline()
m = [1] * len(s)
k = 0
h = ""
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        m[i] = m[i - 1] + 1
    if k < m[i]:
        h = s[i]
        k = m[i]
print(h, max(m))
