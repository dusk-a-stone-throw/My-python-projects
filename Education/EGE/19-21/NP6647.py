def f(s1, s2, m):
    if s1 * s2 >= 123: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s1 + 2, s2, m - 1),
        f(s1 * 2, s2, m - 1),
        f(s1, s2 + 2, m - 1),
        f(s1, s2 * 2, m - 1)
    ]
    return any(h) if (m - 1) % 2 == 0 else all(h)


def f_19(s1, s2, m):
    if s1 * s2 >= 123: return m % 2 == 0
    if m == 0: return 0
    h = [
        f_19(s1 + 2, s2, m - 1),
        f_19(s1 * 2, s2, m - 1),
        f_19(s1, s2 + 2, m - 1),
        f_19(s1, s2 * 2, m - 1)
    ]
    return any(h)


print("N19:")
for s in range(40, 0, -1):
    if f_19(3, s, 2):
        print(s)
        break
answer_20 = []
print("N20:")
for s in range(40, 0, -1):
    if not (f(3, s, 1)) and f(3, s, 3):
        answer_20.append(s)
    if len(answer_20) == 2:
        print(sorted(answer_20))
        break
print("N21:")
for s in range(40, 0, -1):
    if (f(3, s, 2) or f(3, s, 4)) and not (f(3, s, 2)):
        print(s)
        break
