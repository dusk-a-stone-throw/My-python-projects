f = open("P2507.txt")
s = f.readline()
m = 0
k = 1
t = ""
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        k += 1
    else:
        if (k > m):
            t = s[i]
            m = k
        k = 1
print(t, m)
