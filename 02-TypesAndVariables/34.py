speed = int(input("Enter vehicle speed: "))
valid = False

if 40 <= speed <= 140:
    valid = True

print(f"Speed is valid: {valid}")