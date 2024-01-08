arr = [8, 2, 5, 1, 9]
print('Array:',*arr, sep= ' ')
for i in range(len(arr)):
    arr[i] = arr[i]**2
print('2nd power:',*arr, sep= ' ')