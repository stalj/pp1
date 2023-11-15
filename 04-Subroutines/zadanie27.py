import credit_card
a = str(input('Enter card number: '))
if len(a) == 16:
    print(f'Masked card number: {credit_card.f(a)}')
else:
    print('Invalid card number!')