array = [-15,8,-31,47,-2,19]
max=array[0]
min=array[0]

for x in array:
    if(x>max):
        max=x
    if(x<min):
        min=x

print('max:', max)
print('min:', min )