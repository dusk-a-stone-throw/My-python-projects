print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (((y <= x) and (z or w)) <=
                        ((x and not w) or (y == z))):
                    print(x, y, z, w)
