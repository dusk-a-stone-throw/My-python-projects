for A in range(1001, 0, -1):
    flag = True
    for x in range(0, 1001):
        for y in range(0, 1001):
            if not (((x <= 9) <= (x * x <= A)) and ((y * y <= A) <= (y <= 9))):
                flag = False
                break
        if not (flag):
            break
    if flag:
        print(A)
        break
