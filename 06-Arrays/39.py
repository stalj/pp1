arr = [7,3,8,5,2]
arro = []
arre = []

for num in arr:
    if num % 2 == 0:
        arre.append(num)
    else:
        arro.append(num)

arr2 = arre + arro

print(arr2)