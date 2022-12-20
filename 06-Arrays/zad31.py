x=[1,5,2,3,10,22,2,5]

even=[]
odd=[]
for i in x:
    if i%2==0:
        even.append(i)
for i in x:
    if i%2!=0:
        odd.append(i)

print(even)
print(odd)