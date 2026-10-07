text = input("Enter marks with spaces: ")    # 67 45 92 78

marks = []
for part in text.split():
    marks.append(int(part))
if not marks:
    print("Enter marks")
else:
    print(f"Students: {len(marks)}")
    print(f"Highest:  {max(marks)}")
    print(f"Lowest:   {min(marks)}")
    print(f"Total:    {sum(marks)}")
    print(f"Average:  {round(sum(marks) / len(marks), 2)}")
    print(f"Sorted:   {sorted(marks, reverse=True)}")
    

passed = 0
pass_marks = []
for mark in marks:
    pass_marks.append(mark >= 40)
    if mark >= 40:
        passed += 1

if not passed:
    print("Empty marks")
elif all(pass_marks):
    print("Everyone passed")
else:
    print("Not everyone passed")

print(f"Passed: {passed}")

        

