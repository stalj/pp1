array = [15, 8, 31, 47, 2, 19]
length = len(array)
i = 0
sum = 0
j = 0
print("Array: ", end = " ")
while i < length:
    print(array[i] , end =" ")
    i = i + 1

print()
print("arithmetic mean: ", end = " ")

while j < length:
    sum = sum + int(array[j])
    j = j + 1
    
average = sum / length
print(average)
    
