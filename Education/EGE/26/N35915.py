f=open("35915.txt")
n=int(f.readline())
a=list(map(int,f.readlines()))
m_average=0
c=0
b=set(a)
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]%2 != 0 and a[j]%2 != 0 and((a[i]+a[j])//2 in b):
            c+=1
            m_average=max(m_average,(a[i]+a[j])//2)
print(c,m_average)

