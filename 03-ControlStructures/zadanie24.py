a = float(input('Current product price: '))
b = float(input('Previous product price: '))
if a/b <= 0.9:
    print("Buy the product!")
    print(f"Product price reduced by {round((1-a/b)*100, 2)}%")
else:
    print("Don't buy the product!")
    print(f"Product price reduced by {round((1-a/b)*100, 2)}%")