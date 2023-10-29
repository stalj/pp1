password = input("Enter Password: ")
valid = False

if len(password) >= 8:
    valid = True

print(f"Password is valid: {valid}")