Full_name = input("Enter your full name: ").strip().title()
DOB = int(input("Enter your Birth year: "))
Age = 2026 - DOB
is_name = len(Full_name) > 10
print(f"Hi! My name is {Full_name.upper()}. My Birth year is {DOB} and I am {Age} years old.")
print(is_name)