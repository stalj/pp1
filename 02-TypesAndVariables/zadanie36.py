from decimal import*
a = float(input('Bank buys EUR: '))
b = float(input('Bank sells EUR: '))
print(f'Spread: {round(Decimal(abs(a-b)), 4)}')