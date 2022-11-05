pin=int('0805')

for i in range(3):
 wpin=int(input('Wpisz kod pin: '))
 if wpin == pin:
    print('ok')
    break
 elif wpin != pin:
    print("Niepoprawny pin")

if wpin!=pin:
   print("Twoja karta została zablokowana")
 


