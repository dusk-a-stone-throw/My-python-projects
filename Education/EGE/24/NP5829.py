import re
from collections import Counter

s = open("P5829.txt").readline()
# search with overlappings
# Example (without overlapping):
#>>> s="XXPP"
#>>> findall("X.P",s)
#['XXP']
#######
# With overlapping
#>>> s="XXPP"
#>>> findall("(?=(X.P))",s)
#['XXP', 'XPP']
a = re.findall("(?=(X.P))", s)
print(Counter(a).most_common()[0][1])
