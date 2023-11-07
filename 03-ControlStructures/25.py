number_of_products = int(input("Number of products purchased: "))
price = int(input("Product price: "))

amount_to_pay = 0

for thing in range(1, number_of_products + 1):
    if thing > 2:
        amount_to_pay += price * 0.75
    else:
        amount_to_pay += price

print(f"Amount to pay: {amount_to_pay}")

