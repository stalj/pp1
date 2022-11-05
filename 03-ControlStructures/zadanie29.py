suma=0
ilosc=0
srednia=0
while True:
    number=input('Podaj liczbę:')
    if number == '0':
        break
    try:
        y=int(number)
    except:
        print('nie jest liczbą')
        continue
    suma=suma+y
    ilosc=ilosc+1
    srednia=suma/ilosc
print(f'suma liczb: {suma}')
print (f'lacznie liczb: {ilosc}')
print (f'Średnia: {srednia}')

        

