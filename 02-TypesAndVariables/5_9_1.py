liczby=[]
while True:
    a = input("Wpisz liczbe: ")
    try:
        n = int(a)
        liczby.append(n)
    except ValueError:
        if a == "gotowe":
            break
        else:
            print('Liczby pisać!')
            continue

print("Srednia to: ", sum(liczby)/len(liczby))
