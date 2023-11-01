def credit_num():
    number = input("Enter credit card number: ")
    card_number = number[:4]+" "+number[4:8]+" "+number[8:12]+" "+number[12:]
    
    return f'Card number: {card_number}'

print(credit_num())