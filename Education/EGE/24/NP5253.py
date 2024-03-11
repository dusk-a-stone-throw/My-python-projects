s = open("P5253.txt").readline()
s = s.split("2022")
m = 0
for i in range(len(s) - 4):
    c = "2022".join(s[i:i + 5])
    # check if it's possible to add  a 'trail' to the beginning, e.g. 20277772022...
    if ("202" + c).count("2022") <= 4:
        c = "202" + c
    # if it's possible to add to the end, e.g. ...77772022777022...
    if (c + "022").count("2022") <= 4:
        c += "022"
    m = max(m, len(c))
print(m)
