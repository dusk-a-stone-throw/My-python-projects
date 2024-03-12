import re
from collections import Counter
s=open("P4409.txt").readline()
r=re.findall("(?=(CB[^ABF]BC))",s)
c=Counter(i[2:][:-2] for i in r).most_common()
# most common letter
print(c[0][0])
# total number of matches
print(sum(i[1] for i in c))
