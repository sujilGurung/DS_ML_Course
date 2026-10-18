def average(marks):
    try:
        return sum(marks) / len(marks)
    except ZeroDivisionError:
        return 0


def add_mark(marks, text):
    mark = int(text)
    if mark < 0 or mark > 100:
        raise ValueError("Mark must be 0 to 100")
    marks.append(mark)


marks = []

print("Type marks one by one. Type q to finish.")
while True:
    try:
        text = input("Mark (or q to quit): ").strip()
        if text == "":
            raise ValueError("Empty input is not allowed")
    except ValueError as e:
        print("Skipped:", e)
        continue
    if text.lower() == "q":
        break
    try:
        add_mark(marks, text)
    except ValueError as e:
        print("Skipped:", e)

print("Marks:", marks)

avg = average(marks)
print("Average:", round(avg, 1))
if avg >= 40:
    print("Pass")
else:
    print("Fail")

try:
    print("Max mark:", max(marks))
    print("Min mark:", min(marks))
except ValueError:
    print("No marks entered, so there is no max or min")