file = open("27880.txt")
items = file.readlines()
items.pop(0)
items = list(map(int, items))
items.sort()
totalSize = 0
i = 0
while (True):
    if (totalSize + items[i] <= 8358 and i < 2324):
        totalSize += items[i]
    else:
        print(i)
        print(items[i - 1])
        break
    i += 1
