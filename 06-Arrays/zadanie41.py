def f(arr1, arr2):
    for i in arr1:
        if i not in arr2:
            return False
    return  True
arr1 = [3,5,8]
arr2 = [2,8,9,5,3,2,4]
print(f'First array is a subset of a second array: {f(arr1, arr2)}')