f = open("27424_B.txt")
n = int(f.readline())
sum = 0
s = [0]
for i in f:
    a, b = map(int, i.split())
    s = [j + h for j in s for h in (a, b)]
    a1 = [i for i in s if i % 3 == 1]
    a2 = [i for i in s if i % 3 == 2]
    a0 = [i for i in s if i % 3 == 0]
    max1 = max(a1) if len(a1) > 0 else 0
    max2 = max(a2) if len(a2) > 0 else 0
    max0 = max(a0) if len(a0) > 0 else 0
    s = []
    for i in (max1, max2, max0):
        if i != 0:
            s.append(i)
print(max(max1,
          max2))  # max0 mod 3 == 0, don't need it but important for algorithm
