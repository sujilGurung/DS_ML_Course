
while True:
    password = input("Create a password: ")

    has_number = False
    for ch in password:
        if ch.isdigit():
            has_number = True

    if len(password) <= 8:
            print("Password must have 8 letter or more")

    elif not has_number:
            print("Add at least one number in password")

    else:
        print("Strong password saved")
        break

