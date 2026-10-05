def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Can't divide by 0"
    return a / b
def power(a, b):
    return a**b

while True:
    op = input("Choose + - * / ** (or q to quit): ")
    if op == "q":
        print("Bye!")
        break

    x = float(input("First number: "))
    y = float(input("Second number: "))

    if op == "+":
        print(add(x, y))
    elif op == "-":
        print(subtract(x, y))
    elif op == "*":
        print(multiply(x, y))
    elif op == "/":
        print(divide(x, y))
    elif op == "**":
        print(power(x, y))
    else:
        print("Unknown sign")

    match op:
        case "+":
            print(add(x, y))
        case "-":
            print(subtract(x, y))
        case "*":
            print(multiply(x, y))
        case "/":
            print(divide(x, y))
        case "**":
            print(power(x, y))
        case _:
            print("Unknown sign")

