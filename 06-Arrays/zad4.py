import numpy as np
x=np.array(["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"])
print(x)
licznik=0
y=[]
for i in x:
    y.append((len(i)))
print(max(y))