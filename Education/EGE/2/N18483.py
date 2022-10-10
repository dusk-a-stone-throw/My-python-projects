print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((y <= w) == (x <= (not (z)))) and (x or w)):
                    print(x, y, z, w, 1)
print("==============")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (((y <= w) == (x <= (not (z)))) and (x or w)):
                    print(x, y, z, w, 0)
