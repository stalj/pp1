def f(dictionary,average):
    suma=0
    ilosc=len(dictionary["subject"]["grades"])
    wynik=0
    
    for value in dictionary["subject"]["grades"]:
        suma+=value
        wynik=float(suma/ilosc)

    if wynik > average:
        return True
    else:
        return False

        

f({"subject":{"name":"math","grades":[3,3,4]}},3)
