def f(s, m):
    if s >= 25: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + 2, m - 1), f(s * 2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print("N19:")
for s in range(1, 25):
    if f(s, 2):
        print(s)
        break
print("N20:")
answer_20 = []
for s in range(1, 25):
    if not (f(s, 1)) and f(s, 3):
        answer_20.append(s)
print(len(answer_20))
answer_21 = []
print("N21:")
for s in range(1, 25):
    if (f(s, 2) or f(s, 4)) and not (f(s, 2)):
        answer_21.append(s)
    if len(answer_21) == 2:
        break
print(answer_21)
