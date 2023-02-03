f = open("36040_B.txt")
n = f.readline()
s = [0]
for i in f:
    triple = list(map(int, i.split()))
    s = [a + b for a in s for b in triple]
    # values will be overwrited but eventually you get largest ones (mod 109) cuz it's sorted
    s = {j % 109: j for j in sorted(s)}.values() 
print(max(i for i in s if i % 109 != 0))
