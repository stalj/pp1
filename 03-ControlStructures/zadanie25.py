a = int(input('Number of products purchased: '))
b = float(input('Product price: '))
if a > 2:
    print(f'Amount to pay: {2*b+(a-2)*(b*0.75)}')
else:
    print(f'Amount to pay: {a*b}')