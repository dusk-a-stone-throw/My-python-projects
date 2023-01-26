s = "1" * 82
while (s.find("11111") != -1 or s.find("888") != -1):
    if (s.find("11111") != -1):
        s = s.replace("11111", "88", 1)
    else:
        if (s.find("888") != -1):
            s = s.replace("888", "8", 1)

print(s)
