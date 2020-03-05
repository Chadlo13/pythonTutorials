def calculator (num1, num2,op):

    if op == "+":
        print("The addition operation was selected")
        return num1 + num2
    elif op == "/":
        print("The divide operation was selected")
        return num1 / num2
    elif op == "*":
        print("The multiply operation was selected")
        return num1 * num2
    elif op == "-":
        print("The subtraction operation was selected")
        return num1-num2
    else:
        print("Invalid operator")
        return "Invalid operator"

input1 = float(input("Please enter a number: "))
input2 = float(input("Please enter a number: "))
op = input("Please enter one of the following options - + - / *: ")

calcReslut = calculator(input1,input2, op)

if str(calcReslut) != "Invalid operator":
    print("The result of " + str(input1) + op + str(input2) + " is: " + str(calcReslut))
