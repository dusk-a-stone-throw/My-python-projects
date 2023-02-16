import re

pattern = re.compile(".*2.*0.*2.*3.*")
for i in range(2023,
               2023**2 + 1):  # minimum number that match the pattern is 2023
    s = str(i)
    oct_i = oct(i)[2:]
    bin_i = bin(i)[2:]
    if oct_i == oct_i[::-1] and bin_i == bin_i[::-1] and pattern.fullmatch(s):
        print(i, sum(int(x) for x in oct_i))
