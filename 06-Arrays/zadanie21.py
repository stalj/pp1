arr = [15, 8, 31, 47, 2, 19]
arr1 =[]
print('existed array:', *arr, sep = ' ')
for i in range(1,len(arr)+1):
    arr1.append(arr[-i])
print('reverse array:', *arr1, sep = ' ')