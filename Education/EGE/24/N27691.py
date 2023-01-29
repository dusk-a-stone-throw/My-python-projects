f = open("27691.txt")
s = f.readline()
k = 0
m = 0
for i in s:
    if i == "A":
        k += 1
    else:
        m = max(m, k)
        k = 0
print(m)
