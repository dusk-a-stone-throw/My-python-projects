f = open("27890_B.txt")
n = f.readline()
rems = {}
for i in range(0, 5):
    rems[i] = 0
s = [0]
for i in f:
    pair = list(map(int, i.split()))
    s = [a + b for a in s for b in pair]
    for j in s:
        if rems[j % 5] < j:
            rems[j % 5] = j
    s = [i for i in list(rems.values()) if i != 0]
print(max(i for i in rems.values() if i % 5 != 0))
