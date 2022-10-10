print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not ((not (x) == z) <= (y == (w or x))):
                    print(x, y, z, w)
