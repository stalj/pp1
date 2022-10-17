wartosc=int(input("Podaj kwote:"))

coin5=0
coin2=0
coin1=0


if wartosc%5==0:
    coin5=wartosc//5
elif wartosc%2==0:
    coin2=wartosc//2
elif wartosc%1==0:
    coin1=wartosc//1
print(coin5, coin2, coin1)