
name = input("Name: ")
age  = input("Age: ")
city = input("City: ")

student = (name, age, city)     # packing
n, a, c = student                # unpacking
c_lists=list(c)
c_lists[int(input("Enter the index to update list: "))] = input("Enter new value: ")
c = tuple(c_lists)
print(c)


print("===== ID CARD =====")
print("Name:", n)
print("Age :", a)
print("City:", c)

marks = (70, 85, 90)
print(sum(marks))
print(max(marks))
print(min(marks))
