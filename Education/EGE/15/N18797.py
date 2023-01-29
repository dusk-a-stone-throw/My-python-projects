for A in range(500, 0, -1):
    flag = False
    for x in range(1, 500):
        for y in range(1, 500):
            if not ((x > A) or (y > x) or (2 * y + x < 110)):
                flag = True
                break
        if flag:
            break
    if not (flag):
        print(A)
        break
