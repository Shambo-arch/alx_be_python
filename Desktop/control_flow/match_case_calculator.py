num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("choose the operation (+, -, *, /): ")
addition = num1 + num2
difference = num1 - num2
multiplication = num1 * num2
division = num1/num2
match operation:
    case "+":
        print("the result is:", addition)
    case "-":
        print("the result is:", difference)
    case "*":
        print("the result is:", multiplication)
    case "/":
        if num2 == 0:
            print("cannot divide zero")
        else:
            print("the result is:", num1 / num2)
        



