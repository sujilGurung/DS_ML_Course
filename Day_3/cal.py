num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Assigned operator to calculate: +, -, *, /, **: ")

match operator:
    case "+":
        print(f"{num1}+{num2} is: ".strip(), num1+num2)
    case "-":
            print(num1-num2)
    case "*":
            print(num1*num2)
    case "/":
            print(num1/num2)
    case "**":
            print(num1**num2)
    case _:
            print("Please assign correct operator!")