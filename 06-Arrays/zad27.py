x=[5,2,9,6,1]
max=0
for i in x:
    if i>max:
        max=i
min=max
for i in x:
    if i<min:
        min=i
print(min)