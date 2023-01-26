for i in range(35_000_000, 40_000_000 + 1):
    flag = False
    k = 0
    if i % 2 != 0:
        k += 1  # include also this number (i%i==0)
    for j in range(1, round(i * 0.5) + 1):
        if i % j == 0 and j % 2 != 0:
            k += 1
        if k > 5:
            flag = True
            break
    if not (flag) and k == 5:
        print("******", i)
