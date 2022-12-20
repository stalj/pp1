
def computegrade(wartosc):
    if wartosc<0.5:
        print(2.0)
    elif wartosc>=0.5 and wartosc<0.6:
        print(3.0)
    elif wartosc>=0.6 and wartosc<0.7:
        print(3.5) 
    elif wartosc>=0.7 and wartosc<0.8:
        print(4.0)
    elif wartosc>=0.8 and wartosc<0.9:
        print(4.5)
    elif wartosc>=0.9 and wartosc<=1.0:
        print(5.0)
    elif wartosc>1.0:
        print("Wartosc spoza zakresu!")


computegrade(1)