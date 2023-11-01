def cVAT():
    amount = float(input("Enter amount: "))
    vat = round(0.23 * amount, 2)
    result = f"Amount: {amount} \nVAT 23%: {vat}"
    
    return result


print(cVAT())