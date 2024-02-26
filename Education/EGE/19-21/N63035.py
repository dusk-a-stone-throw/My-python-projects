def f(s, m):
    if s >= 96:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s + 1, m - 1)]
    if s % 2 == 0:
        h.append(f(s + s // 2, m - 1))
    if s % 3 == 0:
        h.append(f(s + s // 3, m - 1))
    if s % 2 != 0 and s % 3 != 0:
        h.append(f(s * 2, m - 1))
    return any(h) if (m - 1) % 2 == 0 else all(h)


print("N19")
for s in range(1, 96):
    if f(s, 2):
        print(s)
        break
print("N20")
for s in range(1, 96):
    print(sorted([s for s in range(1, 96) if f(s, 3) and not f(s, 1)], )[-2:])
    break
print("N21")
for s in range(95, 0, -1):
    if (f(s, 2) or f(s, 4)) and not f(s, 2):
        print(s)
        break
