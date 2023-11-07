x= [1,2,3,4,5]

x[0] = x[0] -1
print(x)

x[-1] = x[-1] + 4
print(x)

x[len(x)//2] = x[len(x)//2]*2
print(x)

for i in range(len(x)):
    x[i]= x[i] +4

print(x)