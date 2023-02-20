from fnmatch import fnmatch

f = set(open("P5143.txt").readlines())
k = 0
for i in f:
    i = i.replace("\n", "")
    if fnmatch(i, "195.2*.?*.14"):
        k += 1
print(k)
