def f(s, m):
    if 45 <= s <= 112: return m % 2 == 0
    if s > 112: return m % 2 != 0
    if m == 0: return 0
    h = [f(s + 2, m - 1), f(s * 3, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print("N19:")
for s in range(1, 45):
    if f(s, 2):
        print(s)
        break
print("N20:")
answer_20 = []
for s in range(1, 45):
    if not (f(s, 1)) and f(s, 3):
        answer_20.append(s)
print(len(answer_20))
answer_21 = []
print("N21:")
for s in range(1, 45):
    if (f(s, 2) or f(s, 4)) and not (f(s, 2)):
        answer_21.append(s)
print(min(answer_21), max(answer_21))
