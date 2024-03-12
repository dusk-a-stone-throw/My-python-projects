s = open("P5253.txt").readline()
s = s.split("2022")
m = 0
for i in range(len(s) - 4):
    c = "2022".join(s[i:i + 5])
    # check if it's possible to add  a 'trail' to the beginning, e.g. 20277772022...
    # or at least a part of a 'trail', e.g. 277772022; 02777772022
    if ("2" + c).count("2022") <= 4:
        c = "2" + c
        if ("0" + c).count("2022") <= 4:
            c = "0" + c
            if ("2" + c).count("2022") <= 4:
                c = "2" + c

    # if it's possible to add to the end, e.g. ...77772022777022...
    if (c + "0").count("2022") <= 4:
        c += "0"
        if (c + "2").count("2022") <= 4:
            c += "2"
            if (c + "2").count("2022") <= 4:
                c += "2"

    m = max(m, len(c))
print(m)
