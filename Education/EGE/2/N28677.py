print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x <= y) or (y == w)) and ((x or z) == w):
                    print(x, y, z, w)
