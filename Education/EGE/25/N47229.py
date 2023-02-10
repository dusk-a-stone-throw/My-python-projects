import re

pattern = re.compile("1.2139.*4")
for i in range(2023, 10**10 + 1, 2023):
    if pattern.fullmatch(str(i)) and (i % 2023 == 0):
        print(i, i // 2023)
