import numpy as np

x=np.array([1,2,3,4,5,6,7,8,9,10,11])
licznikp=0
liczniknp=0
for i in x:
    if i%2==0:
        licznikp=licznikp+1
    else:
        liczniknp=liczniknp+1
print(licznikp)
print(liczniknp)