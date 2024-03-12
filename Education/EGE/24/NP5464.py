s=open("P5464.txt").readline()
m=[0]*len(s)
for i in range(2,len(s)):
    if (s[i-2]+s[i-1]+s[i]) in ("BAC", "CAB"):
        m[i]=m[i-3]+3
print(max(m))
