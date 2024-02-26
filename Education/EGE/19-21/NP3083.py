def f(s, m):
    if 36 <= s <= 60: return m % 2 == 0
    if s > 60: return m % 2 != 0
    if m == 0: return 0
    h = [f(s + 1, m - 1), f(s * 2, m - 1), f(s * 3, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print("N19:")
for s in range(1, 36):
    if f(s, 2):
        print(s)
        break
k = 0
print("N20:")
for s in range(1, 36):
    if not (f(s, 1)) and f(s, 3):
        k += 1
print(k)
answer_20 = []
print("N21:")
for s in range(1, 36):
    if (f(s, 2) or f(s, 4)) and not (f(s, 2)):
        answer_20.append(s)
print(min(answer_20), max(answer_20))
