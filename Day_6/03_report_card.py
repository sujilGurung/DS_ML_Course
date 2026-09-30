
name = input("Student name: ")
m1 = int(input("Math: "))
m2 = int(input("Science: "))
m3 = int(input("English: "))

subjects = ["math", "science", "english"]
marks  = dict(zip(subjects, [m1, m2, m3]))
report = {"name": name, "marks": marks}
total = sum(marks.values())
print(f"Total marks: {total}")
avg = total / len(marks)
print(f"Average marks: {avg}")
highest_mark = max(marks, key=marks.get)
print(f"Highest mark: {highest_mark}")
print("===== REPORT CARD =====")
print("Name :", report["name"])
print("Marks:", report["marks"])


