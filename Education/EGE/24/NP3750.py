import re
from collections import Counter
s=open("P3750.txt").readline()
a=[]
for i in range(2,len(s)):
    if s[i-2]==s[i]:
        a.append(s[i-1])
print(Counter(a).most_common()[0])
