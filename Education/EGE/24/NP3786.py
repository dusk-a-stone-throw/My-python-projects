from collections import Counter
s=list(map(lambda x:x.strip(),open("P3786.txt").readlines()))
mmax=0
t=""
for line in s:
    m=[1]*len(line)
    for i in range(1,len(line)):
        if line[i-1]==line[i]:
            m[i]=m[i-1]+1
    if max(m)>mmax:
        mmax=max(m)
        t=line
most_common_letter= Counter(t).most_common()[0][0]
print(most_common_letter,"".join(s).count(most_common_letter))
