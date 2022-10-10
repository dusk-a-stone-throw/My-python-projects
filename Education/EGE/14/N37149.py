a = 4 * 625**9 - 25**15 + 2 * 5**11 - 7
arr = []
while (True):
    rem = a % 5
    a = a // 5
    arr.append(rem)
    if (a < 5):
        break
print(arr)
print(arr.count(4))
