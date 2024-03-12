s=open("P5390.txt").readline()
s=s.replace("B","A").replace("C","A").replace("2","1").replace("3","1")
k=0
m=0
for i in range(2,len(s),3):
    if (s[i-2]+s[i-1]+s[i])=="11A":
        k+=1
    else:
        m=max(m,k)
        k=0
print(m)
