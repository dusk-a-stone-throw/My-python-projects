def GetPrime(a):  # return all prime factors in a list
    s = []
    for i in a:
        if all(i % x != 0 for x in range(2, round(i**0.5) + 1)):
            s.append(i)
    return s


i = 100_000_000 + 1
k = 0
while k < 5:
    rems = set()
    rems.add(i)
    for j in range(2, round(i**0.5) + 1):
        if i % j == 0:
            rems.add(j)
            rems.add(i // j)
    if len(GetPrime(rems)) == sum(1 for i in rems if i % 2 == 0):
        print(i, abs(sum(GetPrime(rems)) - sum(i for i in rems if i % 2 == 0)))
        k += 1
    i += 1
