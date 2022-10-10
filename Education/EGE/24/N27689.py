f = open("27689.txt")
s = f.read()
s = s.replace("XYZ", "v")
k = 0
a = []
for i in range(len(s) - 1):
    if (s[i] == "v"):
        k += 3
    else:
        if (s[i] == "X"):
            k += 1
        if (s[i] == "X" and s[i + 1] == "Y"):
            k += 2
        a.append(k)
        k = 0
print(max(a))
