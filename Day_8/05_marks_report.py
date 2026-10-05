marks = {
    "Ram": 39,
    "Gita": 70,
    "Hari": 80
}
top = 0
topper_name = ""
name = max(marks, key=marks.get)
highest = marks[name]
for mark in marks.items():
    name, score = mark
    
    if score > top:
        top = score
        topper_name = name
    if score >= 40:
        print(f"{name} has Pass")
    else:
        print(f"{name} has Fail")

    if score >=80:
        print(f"{name} grade is A")
    elif score >= 65:
        print(f"{name} grade is B")
    else:
        print(f"{name} grade is C")
   
    
avg = sum(marks.values()) / len(marks)
print(f"The average is: {int(avg)}")
print(f"The topper of the class is {name} scored {highest}")
print(topper_name, top)



