a=[2,4,3,1,7]
even=[]
odd=[]

for x in a:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)

print(even)
print(odd)
