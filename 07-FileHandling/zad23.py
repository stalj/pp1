import re

txt="Tuesday: 22C, Wednesday: 21C, Thursday: 26C"
x=re.findall(r'\d\d\BC',txt)

y=re.findall(r'\d\d',str(x))
suma=0
for i in y:
    suma=suma+int(i)
mean=suma/len(y)
print(mean)