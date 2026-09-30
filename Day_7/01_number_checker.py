number = int(input("Enter a number: "))
if number == 0:
    print("The number is zero: ")
elif number >= 1:
    print("The number is positive: ")
else:
    print("The number is negative: ")

if number % 2 == 0:
    print(f"The {number} is even number")

else:
    print(f"The {number} is odd")