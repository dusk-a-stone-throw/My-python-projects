f = open("17.txt")
a=list(map(int,f.readlines()))
b=list(filter(lambda i:i%2==0,a))
average = sum(b)/len(b)
c=0
m=-100000
for i in range(len(a)-1):
    if (a[i]%3==0 or a[i+1]%3==0) and (a[i] < average or a[i+1] <average):
        c+=1
        m=max(m,a[i]+a[i+1])
print(c,m)
