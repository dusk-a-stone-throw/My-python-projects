s = open("47021.txt").readline()
b = s.split("A")
print(sum([1 for i in b if i.count("B") == 0 if len(i) >= 8]))
