from collections import Counter

s = open("33526.txt").readline()
c = Counter(s[i + 1] for i in range(0, len(s) - 2) if s[i] == s[i + 2])
print(c.most_common()[0][0])
