
lists = []
task  = ""

while task != "quit":
    task = input("Enter the task to do (or quit): ")
    if task != "quit":
        lists.append(task)

print(lists)

count = 0

for task in lists:
    count += 1
    print(f"{count}. {task}")

remove = int(input("Enter finished tasks: "))
lists.pop(remove - 1)

print(f"{remove}. Removed. Remaining tasks: {lists}")

