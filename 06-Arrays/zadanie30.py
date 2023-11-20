def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]
arr3 = [3,6,12,4,34,82]
print(bubblesort(arr1))
print(bubblesort(arr2))
print(bubblesort(arr3))