s = open("P6147.txt").readline()
s = s.split(".")
m = 10 * 100
for i in range(len(s) - 8):
    c = ".".join(s[i:i + 8])
    m = min(m, len(c) - len(s[i]) - len(s[i + 7]))
print(m)
