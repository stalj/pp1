array = [15, 8, 31, 47, 2, 19]
print(*array)

i = 0 
sum = 0
while i<len(array):
    sum = sum + array[i]
    i=i+1
print(sum/len(array))