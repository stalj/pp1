array = [11,42,6,1,5,7,63,68,0]
even = 0
odd = 0
i = 0
while i < len(array):
    if array[i] %2 == 0:
        even += 1
    else:
        odd +=1
    i = i+1

print(f"Even number equals: {even} \nOdd numbers equals: {odd}")

    

