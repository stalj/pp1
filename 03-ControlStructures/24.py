previous_price = float(input("Enter previous price: "))
current_price = float(input("Enter current price: "))

var = 100 - ((current_price/previous_price) * 100)

if current_price < previous_price and var >= 10:
    print("BUY THE THING, DEGENERATE!!!")
    print(f"The price is reduced by {var}%!")