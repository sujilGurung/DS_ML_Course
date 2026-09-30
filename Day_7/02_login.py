users = {"ram": "ram123", "sita": "sita456"}
users["sujil"] = "sujil123"
print("======login credintals========")
name = input("Username: ").strip().lower()
password = input("Password: ")
if name not in users:
    print("User not found")
# elif name == password in users.items():
elif (name, password) in users.items():
    print(f"Welcome, {name.title()}!")
elif not password:
    print("Password is missing")
else:
    print("Wrong password")

print(users)


    # Your job:
# 1. add yourself to the users dictionary
# 2. empty password? print "Password missing"