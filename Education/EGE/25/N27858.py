maxNum = 120114
maxFactors = 0
for i in range(120115, 120200):
    factors = 0
    for j in range(1, i + 1):
        if (i % j == 0):
            factors += 1
    if (factors >= maxFactors):
        maxNum = i
    maxFactors = max(maxFactors, factors)
print(maxFactors, maxNum)
