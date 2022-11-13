def f():
   cena = int(input(f))
   coin5 = cena//5
   coin2 = (cena - 5*coin5)//2
   coin1 = cena - 5*coin5 - 2*coin2
   print(f'Minimum number of coins: ')
   print(coin1+coin2+coin5)

f(23)