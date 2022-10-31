f = open("27421.txt")
s = f.readline()
count = 1
maxCount = 0
for i in range(len(s) - 1):
    if (s[i] != s[i + 1]):
        count += 1
    else:
        maxCount = max(maxCount, count)
        count = 0
print(maxCount)
