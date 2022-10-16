wzrost= float(input("Podaj swój wzrost w cm:"))

wzrost2= wzrost*0,3937
wzrost3= int(wzrost2)//12
wzrost4= wzrost2%12

zdanie=f"Mam {wzrost} cm wzrostu, to jest {wzrost3} stóp i {wzrost4} cali  "
print(zdanie)


