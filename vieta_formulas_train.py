import random
while True:
    arr = [x for x in range(-10, 11) if x != 0]
    random.shuffle(arr)
    x1 = arr[random.randint(0, len(arr) - 1)]
    arr.remove(-x1)
    x2 = arr[random.randint(0, len(arr) - 1)]
    while (True):
        print("x²" + "{0:+}x".format(-(x1 + x2)) + "{0:+}".format(x1 * x2))
        a, b = map(int, input("Enter x₁ and x₂:").split())
        if (a == x1 and b == x2) or (a == x2 and b == x1):
            print("You are right.")
            break
        print("Try again.")
