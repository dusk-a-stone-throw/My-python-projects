from collections import Counter
s=list(map(lambda x: x.strip(), open("P3782.txt").readlines()))
t=""
q=0
for i in s:
    if i.count("Q")>=q:
        t=i
        q=i.count("Q")
less_common_letter=Counter(t).most_common()[-1][0]
print(less_common_letter,"".join(s).count(less_common_letter))
