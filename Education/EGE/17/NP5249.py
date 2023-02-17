f = open("P5249.txt")
a = [int(i) for i in f.readlines()]
tmp = [i for i in a if i % 50 == 0]
average = sum(tmp) / len(tmp)


def PerfectSquare(a):
    return (a**0.5) % 1 == 0


k = 0
m = 10**10
for i in range(0, len(a) - 2):
    s1 = a[i] + a[i + 1]
    s2 = a[i] + a[i + 2]
    s3 = a[i + 2] + a[i + 1]
    if PerfectSquare(s1) and PerfectSquare(s2) and PerfectSquare(s3) and (min(
            s1, s2, s3) > average):
        k += 1
        m = min(a[i] + a[i + 1] + a[i + 2], m)
print(k, m)
