f = open("P6099.txt")
s = f.readline()
r = set()
print("IT'S SLOW AS FK")
for i in range(len(s)):
    k = 0
    digits = {i for i in "0123456789ABCDEF"}
    result = []
    for j in range(i, len(s)):
        if k == 0 and s[j] not in digits:
            break
        result.append(s[j])
        if s[j] in digits:
            k += 1
            digits.remove(s[j])
        if k == 16:
            r.add("".join(result))
            break
print(min([len(i) for i in r]))
print("At long last...")
