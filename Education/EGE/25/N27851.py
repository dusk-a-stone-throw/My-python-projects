for i in range(210_235, 210_300 + 1):
    factors = [j for j in range(2, i // 2 + 1) if i % j == 0]
    if len(factors) == 4:
        print(factors)
