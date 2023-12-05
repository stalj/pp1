def f(arr1, arr2):
    same = None
    if len(arr1) == len(arr2):
        index = 0
        for element in arr1:
            if arr1[index] == arr2[index]:
                same = True
                index += 1
            else:
                same = False
    else:
        same = False
    return same

arr1 = [5,3,1]
arr2 = [5,3]

print(f(arr1,arr2))