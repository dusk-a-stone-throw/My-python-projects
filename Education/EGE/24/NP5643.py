import re
from math import prod

f = open("P5643.txt").readline()
# Had to add overlapping matches using ?=
pattern = re.compile(r"(?=(SS12\d{4}77\d{2}9SS))")
a = str(max(int(i.replace("SS", "")) for i in re.findall(pattern, f)))
print(
    sum(int(i) for i in a if int(i) % 2 != 0) +
    prod(int(i) for i in a if int(i) % 2 == 0))
