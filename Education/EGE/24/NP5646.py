from math import prod
import re
s=open("P5646.txt").readline()
a=re.findall(r"(?=(KK43\d\d78\d\d\d34KK))",s)
a=map(lambda x:x[2:][:-2],a)
print(prod(int(i) for i in str(max(a)) if int(i)%2!=0))
