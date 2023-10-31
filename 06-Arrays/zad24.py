x=[2,3,2,5,8,1,9,8]
y=[]

for i in x:
    if i not in y:
        y.append(i)
        print(i)
print(y)