def f(s1, s2, m):
    if s1 == s2: return m % 2 == 0
    if m == 0: return 0
    h = []
    if s1 < s2:
        h.append(f(s1 + 1, s2, m - 1))
        h.append(f(s1 + 3, s2, m - 1))
    else:
        h.append(f(s1, s2 + 1, m - 1))
        h.append(f(s1, s2 + 3, m - 1))
    return any(h) if (m - 1) % 2 == 0 else all(h)


def f_21(s1, s2, m):
    if s1 == s2: return m % 2 == 0
    if m == 0: return 0
    h = []
    if s1 < s2:
        h.append(f_21(s1 + 1, s2, m - 1))
        h.append(f_21(s1 + 3, s2, m - 1))
    else:
        h.append(f_21(s1, s2 + 1, m - 1))
        h.append(f_21(s1, s2 + 3, m - 1))
    return any(h)


print("N19:")
for s in range(1, 24):
    # if we start with same amount of stones in each heap, it's incorrect!
    # 13 stones if the first heap and 13 in the second -> win on the 0th turn
    if not (f(13, s, 0)):
        if not (f(13, s, 1)) and f(13, s, 2):
            print(s)
            break
print("N20:")
answer_20 = []
for s in range(1, 24):
    if not (f(13, s, 1)) and f(13, s, 3):
        answer_20.append(s)
    if len(answer_20) == 2:
        print(answer_20)
        break
print("N21:")
for s in range(1, 24):
    if not (f(13, s, 2)) and (f(13, s, 2) or f(13, s, 4)) and f_21(13, s, 2):
        print(s)
