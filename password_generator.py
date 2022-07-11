import random

lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$^&*()<>?~"
numbers = "0123456789"
letters = ""  # dynamic string of used symbols


def Gen(letters, length, useSimilar):
    password = ""
    temp = letters
    for i in range(0, length):
        temp = "".join(random.sample(temp, len(temp)))
        randNum = random.randint(0, len(temp) - 1)
        password += temp[randNum]
        if (useSimilar == False):
            temp = temp[:randNum] + temp[randNum + 1:]
    return password


useSymbols = bool(int(input("Use symbols? (1/0): ")))
useNumbers = bool(int(input("Use numbers? (1/0): ")))
useLower = bool(int(input("Use lowercase letters? (1/0): ")))
useUpper = bool(int(input("Use uppercase letters? (1/0): ")))
useSimilar = bool(int(input("Use similar letters? (1/0): ")))

if (useSymbols == useNumbers == useLower == useUpper == False):
    print("Please select at least 1 option!")
    exit(0)
if (useSymbols):
    letters += symbols
if (useNumbers):
    letters += numbers
if (useLower):
    letters += lowerCase
if (useUpper):
    letters += upperCase

length = int(
    input("Enter password length (from 1 to " + str(len(letters)) + "): "))

if (length < 1 or length > len(letters)):
    print("Incorrect length!")
    exit(0)

if (len(letters) < length):
    print("Not enough letters! Max length with current options: " +
          str(len(letters)) + " Add more options.")

amount = int(input("How many passwords do you need?: "))
useWriteToFile = bool(int(input("Write password(s) to a file? (1/0): ")))
if (useWriteToFile):
    file = open(
        "C" + str(amount) + "_L" + str(int(length)) + "_S" +
        str(int(useSymbols)) + "_N" + str(int(useNumbers)) + "_L" +
        str(int(useLower)) + "_U" + str(int(useUpper)) + "_SI" +
        str(int(useSimilar)) + ".txt", "w+")
    for i in range(0, amount):
        file.write(str(Gen(letters, length, useSimilar)) + "\n")
    file.close()
    print("Success!")
else:
    for i in range(0, amount):
        print(Gen(letters, length, useSimilar))
