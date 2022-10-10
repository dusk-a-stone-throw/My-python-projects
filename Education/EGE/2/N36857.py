print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (((not (x) or z) == (y and not (w))) <= (z and y)):
                    print(x, y, z, w)
