def second_largest(arr):
    arr1 = []
    for a in arr:
        arr1.append(a)
    for i in range(len(arr1)):
        for j in range(0, len(arr1)-i-1):
            if arr1[j]>arr1[j+1]:
                arr1[j],arr1[j+1] = arr1[j+1],arr1[j]
    return arr1[-2]

def difference(arr):
    return (max(arr) - min(arr))

def median(arr):
    if len(arr)%2== 0:
        return (arr[len(arr)//2]+arr[(len(arr)//2)+1])/2
    else:
        return arr[len(arr)//2]

def two_element(arr):
    array = [min(arr), max(arr)]
    return ', '.join(map(str, array))

def string(arr):
    return '-'.join(map(str, arr))