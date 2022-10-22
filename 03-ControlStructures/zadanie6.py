predkosc = input("Podaj predkosc samochodu: ")
predkosc = int(predkosc)
ograniczenie = 130
if predkosc > ograniczenie:
    print("Przekroczono predkosc.")
else:
    print("Nieprzekroczono predkosci.")