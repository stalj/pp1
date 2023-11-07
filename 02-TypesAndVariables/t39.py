def discount():
    price = float(input("Enter price: "))
    discount = int(input("Enter discount: "))
    price_with = round(price - price*(discount/100), 2)
    reduction = round(price - price_with, 2)

    result = f'Price with discount: {price_with}\nReduction: {reduction}'

    return result


print(discount())