godzinypracy=float(input("Podaj dlugosc przepracowanych godzin: "))
stawkagodzinowa=float(input("Podaj stawke godzinowa: "))

if godzinypracy>40:
    stawkagodzinowa=stawkagodzinowa*1.5
    print("Zarobiles ", godzinypracy*stawkagodzinowa)
else:
    print("Zarobiles ", godzinypracy*stawkagodzinowa)
