import numpy as np
x=np.array([15,8,31,47,2,19])
suma=0
licznik=0
for i in range(len(x)):
    suma=suma+x[i]
    licznik=licznik+1
print(suma/licznik)