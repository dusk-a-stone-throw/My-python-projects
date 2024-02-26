def f(s1, s2, m):
    if s1 + s2 <= 20: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s1 - 1, s2, m - 1),
        f((s1 + 1) // 2, s2, m - 1),
        f(s1, s2 - 1, m - 1),
        f(s1, (s2 + 1) // 2, m - 1)
    ]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print("N19:")
for s in range(11, 1000):
    if f(10, s, 2):
        print(s)
        break
print("N20:")
answer_20 = []
for s in range(11, 1000):
    if not (f(10, s, 1)) and f(10, s, 3):
        answer_20.append(s)
print(min(answer_20), max(answer_20))
print("N21:")
for s in range(11, 1000):
    if (f(10, s, 2) or f(10, s, 4)) and not (f(10, s, 2)):
        print(s)
