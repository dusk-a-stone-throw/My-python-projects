from collections import Counter

s = open("P5830.txt").readline()
for i in "QWERTYUIOPASDFGHJKLZXCVBNM":
    while 2 * i in s:
        s = s.replace(2 * i, "f{i} {i}")
t = ""
for i in s.split():
    if len(i) >= len(t):
        t = i
print(Counter(t).most_common()[0][1])
