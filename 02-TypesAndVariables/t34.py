def check_speed():
    speed = int(input("Enter vehicle speed: "))
    if speed <= 140 and speed >= 40:
        check = True
    else:
        check = False

    result = f"Speed is valid: {check}"
    
    return result

print(check_speed())