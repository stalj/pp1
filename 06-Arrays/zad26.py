x=[5,1,6,10,3,6,7,8]
max=0
sm=0
for i in x:
    if i>max:
        max=i
print(max)
for i in x:
    if i<max and i>sm:
        sm=i
print(sm)