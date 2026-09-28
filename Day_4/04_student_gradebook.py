gradebook = {
    "Sujil": [48, 50, 90],
    "shyam": [90, 49, 59],
    "Ram": [90, 80, 55]
}

name = input("Enter student name: ")
grade = (input("Enter grade: "))
grades = []
for p in grade.split():
    grades.append(int(p))
if name in gradebook:
    gradebook[name].extend(grades)
else:
    gradebook[name] = grades

averages = []
for student_name, score in gradebook.items():
    avg= sum(score)/len(score)
    averages.append([student_name,avg])

    # 4. Sort highest average first
leaderboard = sorted(averages, key=lambda pair: pair[1], reverse=True)

# 5. Print the leaderboard and the topper
print("Leaderboard:")
for student, avg in leaderboard:
    print(f"{student}: {avg:.1f}")

topper = leaderboard[0]
print(f"Topper: {topper[0]} with {topper[1]:.1f}")