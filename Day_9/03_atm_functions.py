from tabnanny import check


def show_menu():
    print("1. Balance  2. Deposit  3. Withdraw  4. Exit")

def deposit(balance, amount):
    if amount <= 0:
        print("Amount must be more than 0")
        return balance
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        print("Not enough money")
        return balance
    return balance - amount
def check_pin(pin):
    correct_pin = "1234"
    return pin == correct_pin

balance = 1000


while True:
    pin = input("Enter PIN: ")
    if check_pin(pin) == False:
        invalid_attempts = 1
        while invalid_attempts < 3:
            print("Invalid PIN")
            pin = input("Enter PIN: ")
            if check_pin(pin):
                break
            invalid_attempts += 1
        if invalid_attempts == 3:   
            print("Too many invalid attempts. Exiting.")
            break
    
    print("Welcome to the ATM")
    show_menu()
    choice = input("Choose (1-4): ").strip()

    if choice == "1":
        print(f"Balance: Rs. {balance}")
    elif choice == "2":
        amount = int(input("Amount to deposit: "))
        balance = deposit(balance, amount)
    elif choice == "3":
        amount = int(input("Amount to withdraw: "))
        balance = withdraw(balance, amount)
    elif choice == "4":
        print("Thank you! Bye")
        break
    else:
        print("Please choose 1 to 4")

