def f(s1, s2, m):
    if s1 + s2 >= 79: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s1 + 1, s2, m - 1),
        f(s1 + s2, s2, m - 1),
        f(s1, s2 + 1, m - 1),
        f(s1, s2 + s1, m - 1)
    ]
    return any(h) if (m - 1) % 2 == 0 else all(h)


def f_19(s1, s2, m):
    if s1 + s2 >= 79: return m % 2 == 0
    if m == 0: return 0
    h = [
        f_19(s1 + 1, s2, m - 1),
        f_19(s1 + s2, s2, m - 1),
        f_19(s1, s2 + 1, m - 1),
        f_19(s1, s2 + s1, m - 1)
    ]
    return any(h)


print("N19:")
for s in range(1, 70):
    if f_19(9, s, 2):
        print(s)
        break
answer_20 = []
print("N20:")
for s in range(1, 70):
    if not (f(9, s, 1)) and f(9, s, 3):
        answer_20.append(s)
print(min(answer_20), max(answer_20))
print("N21:")
for s in range(1, 70):
    if (f(9, s, 4) or f(9, s, 2)) and not (f(9, s, 2)):
        print(s)
