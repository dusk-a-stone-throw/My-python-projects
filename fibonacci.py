needed = int(input("Enter how many Fibonacci numbers you need: "))
a = 0
b = 1
numbers = [0, 1]
for i in range(0, needed - 2):
    next = a + b
    a = b
    b = next
    numbers.append(next)
print("The first {0} Fibonacci numbers:".format(needed))
for i in range(0, needed):
    print(numbers[i])
