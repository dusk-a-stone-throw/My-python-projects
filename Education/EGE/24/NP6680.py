s = open("P6680.txt").readline()
colors = s.split("#")
hex_digits = "0123456789ABCDEF"
k = 0
for i in colors:
    if len(i) >= 6:
        if all(j in hex_digits for j in i[:6]):
            r = int(i[0] + i[1], 16)
            g = int(i[2] + i[3], 16)
            b = int(i[4] + i[5], 16)
            if r > g and r > b:
                k += 1
print(k)
