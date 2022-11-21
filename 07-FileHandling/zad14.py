filename=input("Podaj nazwe pliku: ")
licznik=0
with open(filename,'r') as f:
    for i in f:
        licznik=licznik+1
print(filename)
print(licznik)