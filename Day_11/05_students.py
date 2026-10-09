def add_student(students, **info):
    students.append(info)
    print(f"Added: {info.get('name', 'Unknown')}")

students = []
add_student(students, name="Ram", age=21, city="Pokhara")
add_student(students, name="Sita", age=22)
add_student(students, age=19, city="Butwal")

for num, s in enumerate(students, start=1):
    if "city" in s:
        print(f"{num}. {s}")
    else:
        print(f"{num}. Students have not city")
    
total_age = 0
for a in students:
    total_age +=a["age"]
average =round (total_age / len(students), 2)
print(f"The average age is {average}")
