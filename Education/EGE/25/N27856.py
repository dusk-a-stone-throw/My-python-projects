factors = []
for i in range(95632, 95651):
    k = 0
    for j in range(1, i + 1):
        if i % j == 0 and j % 2 != 0:
            k += 1
            factors.append(j)
        if k > 6:
            break
    if k == 6:
        print(factors)
    factors.clear()
