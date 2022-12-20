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
print("Max value: ", max(liczby), "Min value: ", min(liczby))