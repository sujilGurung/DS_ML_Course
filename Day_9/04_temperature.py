def c_to_f(c):
    return c * 9 / 5 + 32

def f_to_c(f):
    return (f - 32) * 5 / 9

def is_hot(c):
    return c > 30

print(c_to_f(100))     # 212.0
print(f_to_c(50))      # 10.0
print(is_hot(35))  # True
print(is_hot(25))  # False

choice = input("Convert C to F, or F to C? (c/f): ").strip().lower()
temp = float(input("Temperature: "))

if choice == "c":
    print(f"{temp}°C is {c_to_f(temp)}°F")
elif choice == "f":
    print(f"{temp}°F is {f_to_c(temp)}°C")
else:
    print("Invalid choice")

if is_hot(temp):
    print("It is hot!")
else:
    print("It is not hot.")
