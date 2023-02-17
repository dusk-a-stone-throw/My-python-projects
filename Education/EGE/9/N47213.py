# Had to convert excel table to a txt file
f = open("47213.txt")
k = 0
for i in f:
    a = list(map(int, i.split()))
    # There may be also triplets of unique numbers, ignore them
    unique = [x for x in a if a.count(x) == 1]  # list of all unique numbers
    repeating = [x for x in a
                 if a.count(x) == 2]  # list of all duplicate numbers
    # If i have 4/6 unique numbers, 2 numbers are duplicate (equals each other)
    # For example: a = [1, 2, 3, 4, 5, 5] -> unique = [1, 2, 3, 4] repeating = [5, 5]
    # a= [1, 2, 3, 4, 4, 4] -> unique = [1, 2, 3] repeating = [] (Does not match)
    if len(unique) == 4 and len( # probably do not need to check len of repeating
            repeating) == 2 and sum(unique) / 4 <= sum(repeating):
        k += 1
print(k)
