import numpy as np

x=np.array([[2,5,4],[9,0,3]])
print("a.", x)


print("Length of columns: ", len(x[0]))
print("Length of rows: ", len(x[1]))

for i in x:
    print(i[1])
for i in x:
    print(i[-1])
y=len(x)
for i in range (0,2):
   print(x[i])