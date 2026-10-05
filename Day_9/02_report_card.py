def get_grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 40:
        return "C"
    else:
        return "F"

def average(marks):
    return sum(marks.values()) / len(marks) # this is a line of code

def count_passed(marks):
    count = 0
    for mark in marks.values():
        if mark >= 40:
            count += 1
    return count

def topper_mark(marks):
    name = max(marks, key=marks.get)
    topMark = marks[name]
    return f"{name} has secured the highest mark of {topMark}"

    
marks = {"Ram": 78, "Sita": 92, "Hari": 35, "Gita": 64}
for name, mark in marks.items():
    print(f"{name}: {mark} -> {get_grade(mark)}")

print(f"Class average: {average(marks)}")

count = count_passed(marks)
print(count)
print(topper_mark(marks))
