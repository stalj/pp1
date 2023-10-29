buy = float(input("Bank buys EUR: "))
sell = float(input("Bank sells EUR: "))

spread = round(sell-buy, 4)

print(f"Spread: {spread}")