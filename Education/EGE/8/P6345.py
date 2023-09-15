from itertools import permutations

k = 0
for i in set(permutations("ВАРФОЛОМЕЙ", 6)):
    if len(set(i)) == 6:
        s = "".join(i)
        for i in "ВРФЛМЙ":
            s = s.replace(i, "c")
        for i in "АОЕ":
            s = s.replace(i, "v")
        if (s.count("c") > s.count("v")) and "vv" not in s:
            k += 1
print(k)
