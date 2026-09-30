age = int(input("Your age: "))

if age >= 18:
    print("You can vote")
    print("Bring your ID card")

print("Thank you!")      # always runs

marks = 45

if marks >= 40:
    print("Passed")         # inside the if
    print("Well done")      # inside the if
print("Result checked")     # outside: always runs


if marks >= 40:
    print("Passed")

age = int(input("Your age: "))

if age >= 18:
    print("You can vote")
else:
    print("Too young to vote")

    marks = int(input("Your marks: "))

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")

marks = 90

# Wrong order
if marks >= 40:
    print("Grade C")       # runs, and stops here
elif marks >= 80:
    print("Grade A")       # never checked

# Right order
if marks >= 80:
    print("Grade A")       # runs
elif marks >= 40:
    print("Grade C")


