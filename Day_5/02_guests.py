
ram  = set(input("Ram's guests: ").split(","))
sita = set(input("Sita's guests: ").split(","))

print("On both lists:", ram & sita)
print("All guests   :", ram | sita)
print(len(ram))
print(len(sita))
print(ram - sita)
print("Hari" in ram)
guests = input("Enter Ram or Sita as per their guest: ").lower()
if "ram" in guests:
    ram.add(input("Enter rams new guest name: "))
elif "sita" in guests:
    sita.add(input("Enter Sitas new guest name: "))
else:
    print("Invalid name")

g = input("Enter Ram or Sita as per their guest to discard: ").lower()
if "ram" in g:
    ram.discard(input("to discard: "))
elif "sita" in g:
    sita.discard(input("to discard: "))
else:
    print("Invalid name: ")
print("Total guests:", len(ram | sita))
