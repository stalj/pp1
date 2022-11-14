array = [2,3,7,5,4]
print(array)
print(len(array))
print(array[0])
print(array[1])
print(array[-1]) #array[len(array)-1]
print(array[-2])
#print(array.sum())
arr_sum = array[0] + array[-1]
print(arr_sum)

print(array[2]) # or array[int(len(array)/2)]

for i in array:
    print(i, end = ' ')
print()

for i in range(0, int(len(array)/2)+1):
    print(array[i], end=' ')
