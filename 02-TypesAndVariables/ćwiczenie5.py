suma=0
ilosc=0
max = None
min = None
while True:
    zbior = input ('Podaj liczbe:')
    if zbior == 'done':
        break
    try:
        y=int (zbior)
    except:
        print('zte dane')
        continue
    ilosc=ilosc+1
    suma=suma + y
    if max is None or y > max:
        max = y
    if min is None or y < min:
        min = y
print (f'lacznie liczb: {ilosc}')
print (f'suma liczb: {suma}')
print (f'najwieksza liczba: {max}')
print (f'najmniejsza liczba: {min}')