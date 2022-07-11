f = open("27687.txt")
text = f.read()
count = 0
maxC = 0
for i in range(0, len(text)):
    if (text[i] == "Y"):
        count += 1
    else:
        maxC = max(maxC, count)
        count = 0
print(maxC)
