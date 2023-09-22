suma=0
x=0
while True:
    a=int(input("Podaj liczbę:"))
    if a==0:
        break
    else:
        suma+=a
        x+=1

srednia=suma/x
print(f"Suma podanych liczb wynosi {suma}, a ich średnia {srednia}")