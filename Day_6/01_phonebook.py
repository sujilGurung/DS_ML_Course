

contacts = {"Ram": "9801111111", "Sita": "9802222222"}

name  = input("New contact name: ")
phone = input("Phone number: ")
contacts[name] = phone              # add it

print("All contacts:", contacts)
print("Total:", len(contacts))

find = input("Search a name: ")
print("Number:", contacts.get(find, "Not found"))
remove = input("Remove item: ")
print(f"remove items from dictonary: {contacts.pop(remove, 'invalid name')}")
print(f"Only names: {list(contacts.keys())}")

