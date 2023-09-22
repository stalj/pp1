def identity_matrix(n):
    arr = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        arr[i][i]=1
    return arr

arr = identity_matrix(3)

for i in arr:
    print(i)
print()
