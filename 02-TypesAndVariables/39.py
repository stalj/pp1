price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))
discount /= 100

reduction = round(price * discount, 2)

print(f"Price with discount: {round(price - reduction, 2)}\nReduction: {reduction}")