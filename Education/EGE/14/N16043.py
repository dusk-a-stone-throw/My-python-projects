a = 9**7 + 3**21 - 9
s = ""
while a > 0:
    s = str(a % 3) + s
    a //= 3
print(s.count("2"))
