def calculator ():
    print("simple calculator")
    print("opetation:+,-,*,/")

    try:
        num1 = float(input("enter the first number:"))
        num2 = float(input("enter the Second number:"))
        operation = input("enter operation(+,-,*,/):")

        if operation =='+':
            result = num1 + num2
        elif operation == '-':
            result == num1 - num2 
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 ==0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2 
        else:
            print("invalid operation")
            return
        print(f"result:{result}")
    except ValueError:
        print("Invaild input ! please enter numeric values")
calculator()