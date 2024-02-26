def f(s1, s2, m):
    if s1 + s2 >= 45: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s1 + 2, s2, m - 1),
        f(s1 * 3, s2, m - 1),
        f(s1, s2 + 2, m - 1),
        f(s1, s2 * 3, m - 1)
    ]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print("N19:")
k = 0
#i+j<=43
for i in range(1, 43):
    for j in range(1, 43 - i + 1):
        if f(i, j, 2) and not f(i, j, 0):
            k += 1
print(k)
print("N20:")
answer_20 = []
for i in range(1, 43 - 4 + 1):
    if i + 4 <= 43:
        if f(4, i, 3) and not (f(4, i, 1)):
            answer_20.append(i)
print(min(answer_20), max(answer_20))
print("N21:")
for i in range(1, 43 - 13 + 1):
    if i + 13 <= 43:
        if (f(13, i, 2) or f(13, i, 4)) and not (f(13, i, 2)):
            print(i)
