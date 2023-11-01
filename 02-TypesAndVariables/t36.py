def spread():
    buyeur = round(float(input("Bank buys EUR: ")), 4)
    selleur = round(float(input("Bank sell EUR: ")), 4)
    spread = round(selleur - buyeur, 4)
    result = f'Spread: {spread}'

    return result

print(spread())
