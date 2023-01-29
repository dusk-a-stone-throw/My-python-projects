f = open("27991_B.txt")
n = int(f.readline())
even17 = []  # even and % 17 == 0
odd17 = []  # odd and % 17 == 0
even = []  # % 17 != 0
odd = []
for s in f:
    a = int(s)
    if (a % 2 == 0):
        if (a % 17 == 0):
            even17.append(a)
        else:
            even.append(a)
    else:
        if (a % 17 == 0):
            odd17.append(a)
        else:
            odd.append(a)
# even17 is actually empty in 27991_A
# WARNING: according the task, print pair ASCENDING
# default=-1000 to ignore the empty list
print(
    sorted((max(even17, default=-1000), max(even)), reverse=True) if (
        max(even17, default=-1000) + max(even) > max(odd17) + max(odd)) else (
            sorted((max(odd17), max(odd)), reverse=True)))
