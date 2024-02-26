def f_19(s1, s2, m):
    if s1 + s2 >= 45: return m % 2 == 0
    if m == 0: return 0
    h = [
        f_19(s1 + 1, s2, m - 1),
        f_19(s1 * 3, s2, m - 1),
        f_19(s1, s2 + 1, m - 1),
        f_19(s1, s2 * 3, m - 1)
    ]
    # any instead of all
    return any(h)


def f(s1, s2, m):
    if s1 + s2 >= 45: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s1 + 1, s2, m - 1),
        f(s1 * 3, s2, m - 1),
        f(s1, s2 + 1, m - 1),
        f(s1, s2 * 3, m - 1)
    ]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print("N19:")
for s in range(1, 41):
    if f_19(4, s, 2):
        print(s)
        break
print("N20:")
for s in range(1, 41):
    if not (f(4, s, 1)) and f(4, s, 3):
        print(s)
print("N21:")
for s in range(1, 41):
    if (f(4, s, 2) or f(4, s, 4)) and not (f(4, s, 2)):
        print(s)
