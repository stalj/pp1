def f(arr):
    i=0
    for x in arr:
        j=0
        for y in x:
            if arr[i][j]!=((i+1)*(j+1)):
                return False
            j+=1
        i+=1
    return True

print(f([[1,2,3],[2,4,6],[3,6,9]]))
print(f([[1,2],[2,4]]))
print(f([[1,2],[3,6]]))
print(f([[1,2,3],[2,5,6]]))
print(f([[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]]))