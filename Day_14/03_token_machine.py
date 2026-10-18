def token_machine(prefix):
    n = 1
    while True:
        yield f"{prefix[0].upper()} - {n}"
        n += 1


while True:
    person = input("Are you VIP or normal: ").strip().lower()
    if person in ("vip", "normal"):
        break
    print("Enter only VIP or normal")

tokens = token_machine(person)

print("=== Bank Token Machine ===")
while True:
    choice = input("Press Enter for a token (q to quit): ")
    if choice.lower() == "q":
        print("Bye!")
        break
    print("Your token:", next(tokens))

def countdown(n):
    for i in range(n, 0, -1):
        yield i


n = int(input("Enter a number: "))
print("Next in", end=" ")
for num in countdown(n):
    print(num, end=" ")
print()
