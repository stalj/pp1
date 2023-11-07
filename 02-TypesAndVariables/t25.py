def paying_taxes():
    taxes = True
    age = int(input("Enter age: "))
    if age > 26:
        taxes = False
    return f"Exemption from paying taxes: {taxes}"

print(paying_taxes())