import re

f=open('zad_27.txt','r')
f_content=f.read()

numbers=re.findall("\d.\d",f_content)
print(numbers)
suma=0
ilosc=len(numbers)
print(ilosc)
for x in numbers:
    suma+=int(x)

print(suma)
srednia=suma/ilosc
print(srednia)
f.close()