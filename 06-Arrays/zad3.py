import numpy as np

x=np.array([-15, 8, -31, 47, -2, 19])
print("maximum: ", max(x))
print("minimum: ", min(x))

min=x[0]
max=x[0]
for i in range(0, len(x)):    
   if(x[i] < min):    
       min = x[i]
print("minimum: ", min)
for i in range(0, len(x)):    
   if(x[i] > max):    
       max = x[i]
print("maximum: ", max)