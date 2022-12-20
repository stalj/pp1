import numpy as np
x=np.array([[True,False],[True,True],[False,False]])
for i in range (3):
    if x[i][i]==True:
        x[i][i]=False
    else:
        x[i][i]=True
print(x)