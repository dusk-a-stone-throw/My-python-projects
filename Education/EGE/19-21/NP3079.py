def f(s, m):
    if s > 33: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + 1, m - 1), f(s + 2, m - 1), f(s + 3, m - 1), f(s * 2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print("N19:")
for s in range(1, 34):
    if f(s, 2):
        print(s)
print("N20:")
answer_20 = []
for s in range(1, 34):
    if not (f(s, 1)) and f(s, 3):
        answer_20.append(s)
print(min(answer_20), max(answer_20))
print("N21:")
for s in range(1, 34):
    if (f(s, 2) or f(s, 4)) and not (f(s, 2)):
        print(s)
