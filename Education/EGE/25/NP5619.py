from fnmatch import fnmatch
# let x = pq + r where r is remainder of division by p
# (x - x % p ) % p == 0 because (pq + r - r) == pq
for i in range(1010101 - 1010101 % 4023, 1898989 + 1, 4023):
    # a number that matching mask: 1EOEOEO where E - even, O - odd
    if fnmatch(str(i), "1[02468][13579][02468][13579][02468][13579]"):
        print(i, i // 4023)
