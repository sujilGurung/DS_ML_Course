# def get_number(question):
#     answer = input(question).strip()
#     while True:
#         if answer == 1 and 120 >= answer:
#             if answer.isdigit():
#                 return int(answer)
#             print("Please type a number only")
#         else:
#             break
# age = get_number("Your age: ")
# print(f"Next year you will be {age + 1}")

# Your age: twenty
# Please type a number only
# Your age: 20
# Next year you will be 21

# Your job:
# 1. only accept ages from 1 to 120
# 2. use get_number() in the Day 09 calculator



def get_number(question, min_val = 1, max_val = 120):
    while True:
        answer = input(question).strip()
        if not answer.isdigit():
            print("Please type a number only")
        elif not (min_val <= int(answer) <= max_val):
            print(f"Please enter a number between {min_val} and {max_val}")
        else:
            return int(answer)

def get_float(question):
    answer = input((question).strip())
    check = answer
    if check.startswith("-"):
        check = check[1:]
    elif check.count(".")<= 1 and check.replace(".", "").isdigit() and check != "":
        return float(answer)
    else:
        print("Enter only number")

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
    return pow(a, b)


age = get_number("Your age: ")
print(f"Next year you will be {age + 1}")

while True:
    op = input("Choose + - * / ** (or q to quit): ")
    if op == "q":
        print("Bye!")
        break

    x = get_float("First number: ")
    y = get_float("Second number: ")

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


    

            



# Your age: twenty
# Please type a number only
# Your age: 20
# Next year you will be 21

# Your job:
# 1. only accept ages from 1 to 120
# 2. use get_number() in the Day 09 calculator