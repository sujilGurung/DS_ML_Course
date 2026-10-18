def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please type a number.")

print("=== Safe Calculator ===")

again = "y"
while again =="y":
    a = get_number("First number: ")
    op = input("Choose + - * / % ** : ")
    b = get_number("Second number: ")
    
    try:
        if op == "+":
            print("Answer:", a + b)
        elif op == "-":
            print("Answer:", a - b)
        elif op == "*":
            print("Answer:", a * b)
        elif op == "/":
            print("Answer:", a / b)
        elif op == "%":
            print("Answer:", a % b)
        elif op == "**":
            print("Answer:", pow(a, b))
        else:
            print("Unknown sign:", op)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    
    again = input("Again want to calculate (y/n): ").strip().lower()
    

