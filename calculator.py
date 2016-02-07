#Simple Calculator(Add, Subtract, Divide, Multiply)
def add(x, y):
    print ("This adds two numbers")
    return x + y
def subtract(x, y):
    print ("This subtracts two numbers")
    return x - y
def divide(x, y):
    print ("This divides two numbers")
    return x / y
def multiply(x, y):
    print ("This multiplies two numbers")
    return x * y

while 1 == 1:
    print ("Pick One")
    print ("a. Add")
    print ("b. Subtract")
    print ("c. Divide")
    print ("d. Multiply")

    choice = input("Choose a, b, c, or d:" )

    if (choice != "a" and choice != "b" and choice != "c" and choice != "d"):
        print ("Invalid Character")
        continue

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    if choice == "a":
        print (add(num1, num2))
    elif choice == "b":
        print (subtract(num1, num2))
    elif choice == "c":
        print (divide(num1, num2))
    elif choice == "d":
        print (multiply(num1, num2))
    else:
        print ("Invalid Character")
    



    




