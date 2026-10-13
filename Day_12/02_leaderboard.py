students = [
    {"name": "Ram", "marks": 78},
    {"name": "Sita", "marks": 92},
    {"name": "Hari", "marks": 35},
    {"name": "Gita", "marks": 85},
    {"name": "Anil", "marks": 28},
]

ranked = sorted(students, key=lambda s: s["marks"], reverse=True)

print("=== Leaderboard ===")
for rank, s in enumerate(ranked, start=1):
    status = "Pass" if s["marks"] >= 40 else "Fail"
    print(f"{rank}. {s['name']}: {s['marks']} ({status})")

passed = list(filter(lambda s: s["marks"] >= 40, students))
names = list(map(lambda s: s["name"], passed))
print("Passed:", ", ".join(names))
print(f"Pass rate: {len(passed)} of {len(students)}")
print("----class Average-----")
average = list(map(lambda s: s["marks"], students))
print(f"Average marks: {sum(average) // len(average)}")
def add_student(students, name, marks):
    students.append({"name": name, "marks": marks})
    

add_student(students, name="Sujil", marks=90)
print(students)
# === Leaderboard ===
# 1. Sita: 92 (Pass)
# 2. Gita: 85 (Pass)
# 3. Ram: 78 (Pass)
# 4. Hari: 35 (Fail)
# 5. Anil: 28 (Fail)
# Passed: Ram, Sita, Gita
# Pass rate: 3 of 5

# Your job:
# 1. print the class average
#    (hint: map() the marks, then sum() and len())
# 2. write add_student(name, marks) with def (Day 09)
#    that appends a new dictionary to students