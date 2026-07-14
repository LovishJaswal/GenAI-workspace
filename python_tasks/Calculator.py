print("\nWelcome to the calculator!\n")
terminate = None
while(True):
    if terminate == "quit":
        break
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    op = input("Enter the operand: ")
    if op == "+":
        print (num1+num2)
    elif op == "-":
        print(num1-num2)
    elif op == "*":
        print(num1*num2)
    elif op == "/":
        if num2 != 0:
            print(num1/num2)
        else:
            print("Can't divide by zero!")
    elif op == "%":
        if num2!=0:
            print(num1%num2)
        else:
            print("Can't divide by zero!")
    terminate = input("Type 'quit' to quit or press any key to continue: ")