def f(s1,s2,m):
    if s1+s2>=231: return m%2==0
    if m==0: return 0
    h=[f(s1+2,s2,m-1), f(s1*2,s2,m-1), f(s1,s2+2,m-1), f(s1,s2*2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
def f_19(s1,s2,m):
    if s1+s2>=231: return m%2==0
    if m==0: return 0
    h=[f_19(s1+2,s2,m-1), f_19(s1*2,s2,m-1), f_19(s1,s2+2,m-1), f_19(s1,s2*2,m-1)]
    return any(h)

print("N19:")
answer_19=[]
for s in range(1,214):
    if f_19(17,s,2):
        answer_19.append(s)
print(max(answer_19))
answer_20=[]
print("N20:")
for s in range(1,214):
    if not(f(17,s,1)) and f(17,s,3):
        answer_20.append(s)
print(min(answer_20),max(answer_20))
print("N21:")
for s in range(1,214):
    if (f(17,s,2) or f(17,s,4)) and not(f(17,s,2)):
        print(s)
        break
