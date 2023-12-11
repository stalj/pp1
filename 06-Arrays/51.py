arr = [[1,1,1,1,1],
       [0,0,0,0,0],
       [2,2,2,2,2]]

arr2 = arr[0]
arr3 = arr[len(arr) - 1]

arr[0] = arr3
arr[len(arr) - 1] = arr2

print(arr)