age = 16
city = "Pokhara"
friends = ["Ram", "Sita"]

if age >= 18 and city == "Pokhara":
    print("A")
elif age >= 18 or city == "Pokhara":
    print("B")
else:
    print("C")

if "Hari" not in friends:
    print("Hari is new")

if friends:
    print("You have friends")