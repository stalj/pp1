import numpy as np
i=0
x=([15,8,31,47,2,19])
total=x
sum=0
while(i < len(x)):
    sum = sum + x[i]
    i = i+1
print(sum/len(x))