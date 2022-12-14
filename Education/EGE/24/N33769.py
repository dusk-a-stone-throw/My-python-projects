from collections import Counter

f = open("33769.txt")
a = f.readline()
symbols = []
for i in range(len(a) - 2):
    if (a[i] == a[i + 1]):
        symbols.append(a[i + 2])
data = Counter(symbols)
print(data.most_common(1)[0][0])
