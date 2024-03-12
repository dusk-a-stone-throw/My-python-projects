s = list(map(int, open("46975.txt").readlines()))
even = [i for i in s if i % 2 == 0]
average_even = sum(even) / len(even)
k = 0
m = -100
for i in range(len(s) - 1):
    a = s[i]
    b = s[i + 1]
    if (a % 3 == 0 and b < average_even) or (b % 3 == 0 and a < average_even):
        k += 1
        m = max(m, a + b)
print(k, m)
