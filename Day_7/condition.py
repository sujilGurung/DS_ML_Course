age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Enjoy the movie")      # both True

day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("Holiday!")             # one is True

is_raining = False
if not is_raining:
    print("Let's play outside")   # not False = Truev

fruits = ["apple", "mango", "banana"]
if "mango" in fruits:
    print("We have mango")

email = "ram@gmail.com"
if "@" not in email:
    print("Invalid email")
else:
    print("Email looks OK")

prices = {"tea": 20, "coffee": 50}
item = input("Order: ")
if item in prices:
    print(f"Price: Rs. {prices[item]}")
else:
    print("Sorry, not on the menu")

answer = input("Do you like Python? ")

if answer.strip().lower() == "yes":
    print("Great! Me too")
else:
    print("You will soon!")

# yes, YES and " Yes " all print: Great! Me too

name = input("Your name: ")
if len(name) > 10:
    print("That is a long name")

name = input("Your name: ")

if name:
    print(f"Hello, {name}")
else:
    print("You didn't type anything")

cart = []
if not cart:
    print("Your cart is empty")

print(bool(0), bool(""), bool([]))       # False False False
print(bool(5), bool("hi"), bool([1]))    # True True True

username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "1234":
        print("Welcome, admin!")
    else:
        print("Wrong password")
else:
    print("User not found")

day = input("Day: ")

# with if / elif
if day == "sat":
    print("Holiday")
elif day == "fri":
    print("Half day")
else:
    print("School day")

# with match-case (Day 03)
match day:
    case "sat":
        print("Holiday")
    case "fri":
        print("Half day")
    case _:
        print("School day")