f = open("27424_A.txt")
a = f.readlines()
n = int(a[0])
a.pop(0)
for i in range(n):
    x, y = map(int, a[i].split())
    print(x, y)
