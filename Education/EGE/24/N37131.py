file = open('37131.txt', 'r')
st = file.readline()
k = 1
mx = 0
for i in range(1, len(st)):
    if (st[i] == 'K' and st[i - 1] == 'L') or (st[i - 1] == 'K'
                                               and st[i] == 'L'):
        k = 1
    else:
        k += 1
        if k > mx:
            mx = k
print(mx)
