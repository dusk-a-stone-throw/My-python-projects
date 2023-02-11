f = open("47228.txt")
a = f.readline()
k = 0
m = 0
for i in range(0, len(a) - 1, 2):
    if a[i] in "CDF" and a[i + 1] in "AO":
        k += 1
        m = max(m, k)
    else:
        k = 0
print(m)
