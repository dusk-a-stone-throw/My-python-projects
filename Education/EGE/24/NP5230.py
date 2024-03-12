s=open("P5230.txt").readline()
for i in "EIOUY":
    s=s.replace(i,"A")
s=s.split("A")
for i in range(len(s)-6):
    c="A".join(s[i:i+6])
    m=max(m,len(c))
print(m)
