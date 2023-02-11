k = 0
for i in range(245_690, 245_756 + 1):
    k += 1
    if all(i % j != 0 for j in range(2, round(i ** 0.5) + 1)):
        print(k, i)
