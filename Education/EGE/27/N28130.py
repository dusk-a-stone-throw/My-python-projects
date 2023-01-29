from math import comb

f = open("28130_B.txt")
n = int(f.readline())
# remainders for numbers >50 of division by 80
more_than_50_remainders = [0] * 80
less_or_equal_50_remainders = [0] * 80
count = 0
for s in f:
    i = int(s)
    if i > 50:
        more_than_50_remainders[i % 80] += 1
    else:
        less_or_equal_50_remainders[i % 80] += 1
# for i in range(40):
#     print(list(more_than_50_remainders.items())[i])
#     print(
#         list(less_or_equal_50_remainders.items())[
#             len(less_or_equal_50_remainders) - 1 - i])
#     print("========")
#     input()
#     count += more_than_50_remainders[i] * less_or_equal_50_remainders[
#         len(less_or_equal_50_remainders) - 1 - i]
for i in range(1, 40):
    count += more_than_50_remainders[i] * less_or_equal_50_remainders[-i]
    count += more_than_50_remainders[-i] * less_or_equal_50_remainders[i]
    count += more_than_50_remainders[i] * more_than_50_remainders[-i]
count += more_than_50_remainders[0] * less_or_equal_50_remainders[0] + comb(
    more_than_50_remainders[0], 2)
# fourties elements also % 80 == 0, so we need to choose two of them
count += more_than_50_remainders[40] * less_or_equal_50_remainders[40] + comb(
    more_than_50_remainders[40], 2)
print(count)
