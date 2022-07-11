while(True):
    a = float(input("Enter the first term: "))
    b = float(input("Enter the second term: "))
    operation = input("Enter a operator (+,-, *, /, **), enter \"EXIT\" to exit: ")
    match operation:
        case "+":
            print(a + b)
        case "-":
            print(a - b)
        case "*":
            print(a * b)
        case "**":
            print(a ** b)
        case "/":
            if(b == 0):
                print("Division by 0!")
            else:
                print(a / b)
        case "EXIT":
            exit()
