cena = 23
coin5 = cena//5
coin2 = (cena - 5*coin5)//2
coin1 = cena - 5*coin5 - 2*coin2
print(f'The amount of PLN {cena} in coins:  ')
print(f'5 zł - {coin5}')
print(f'2 zł - {coin2}')
print(f'1 zł - {coin1}')
