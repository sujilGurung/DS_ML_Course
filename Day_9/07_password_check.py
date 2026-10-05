def has_number(password):
    for ch in password:
        if ch.isdigit():
            return True
    return False

def has_capital(password):
    for ch in password:
        if ch.isupper():
            return True
    return False

def is_strong(password):
    return len(password) >= 8 and has_number(password) and has_capital(password)

while True:
    password = input("New password: ")
    if is_strong(password):
        print("Strong password. Saved!")
        break
    print("Use 8 or more letters and at least one number")
    print("and at least one capital letter.")