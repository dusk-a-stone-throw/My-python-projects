def f(s1, s2, m):
    if s1 + s2 >= 77: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s1 + 1, s2, m - 1),
        f(s1 * 2, s2, m - 1),
        f(s1, s2 + 1, m - 1),
        f(s1, s2 * 2, m - 1)
    ]
    return any(h) if (m - 1) % 2 == 0 else all(h)


def f_19(s1, s2, m):
    if s1 + s2 >= 77: return m % 2 == 0
    if m == 0: return 0
    h = [
        f_19(s1 + 1, s2, m - 1),
        f_19(s1 * 2, s2, m - 1),
        f_19(s1, s2 + 1, m - 1),
        f_19(s1, s2 * 2, m - 1)
    ]
    return any(h)


print("N19:")
for s in range(1, 70):
    if f_19(7, s, 2):
        print(s)
        break
print("N20:")
for s in range(1, 70):
    if f(7, s, 3) and not (f(7, s, 1)):
        print(s)
print("N21")
for s in range(1, 70):
    if (f(7, s, 4) or f(7, s, 2)) and not (f(7, s, 2)):
        print(s)
        break
