f = open("P6147.txt")
s = f.readline()
r = set()
for i in range(len(s)):
    t = ""
    k = 0
    for j in range(i, len(s)):
        # no need to check substrings that don't start with "."
        if k == 0 and s[j] != ".":
            break
        t += s[j]
        if s[j] == ".":
            k += 1
        if k == 7:
            r.add(t)
            break
print(min([len(i) for i in r]))
