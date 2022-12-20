import numpy as np

x=np.array([2, 3, 7, 5, 4])
print(x)
for i in x:
    print(i)
print("Number of elements: ", len(x))
print("First elements: ", x[0])
print("Last element: ", x[-1])
print("Last but one: ", x[-2])
print("Middle element: ", x[-3])
print("Sum of first and last value: ", x[0]+x[-1])
'''for i in x:
   print(i, end=' ') 
'''
print(" ".join(str(i) for i in x))

print(" ".join(str(x[i]) for i in range(0,3)))
