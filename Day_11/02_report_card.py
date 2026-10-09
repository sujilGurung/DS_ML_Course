def report_card(name, **marks):
    passed = []

    print(f"===== {name} =====")
    for subject, mark in marks.items():
        if mark >= 40:
            result = "Pass"
        else:
            result = "Fail"
        print(f"{subject}: {mark} ({result})")
        passed.append(mark >= 40)

    total = sum(marks.values())
    average = round(total / len(marks), 2)
    best = max(marks, key=marks.get)

    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Best subject: {best}")

    if all(passed):
        print("Promoted!")


report_card("Sita", math=88, science=35, english=91, nepali=72)

ram_marks = {"math": 78, "science": 96, "english": 78, "nepali": 88}
report_card("Ram", **ram_marks)