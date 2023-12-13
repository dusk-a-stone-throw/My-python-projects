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
        # we can remove one element and
        # replace it with the largest element we are able to
        for j in sorted(items, reverse=True):
            if 8358 - (totalSize - items[i - 1]) >= j:
                print(j)
                break
        break
    i += 1
