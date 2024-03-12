import re
s=open("P3530.txt").readline()
print(sum(len(re.findall("(?=(A.{"+str(i)+"}F))",s)) for i in range(5,9)))
