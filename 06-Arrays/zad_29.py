def f(arr,x):
    for y in range(len(arr)):
        z=arr[y]+x
        arr[y]=z
    return arr

a=[2,4,6,8]
print(f(a,1))
