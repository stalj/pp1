def transpose_matrix(m):
    arr = [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]
    return arr
#a
m = [[1,2,3],[4,5,6],[7,8,9]]
arr = transpose_matrix(m)
for i in arr:
    print(i)
print()
#b
m = [[1, 2, 3, 4, 5],[6, 7, 8, 9, 0]]
arr = transpose_matrix(m)
for i in arr:
    print(i)
print()
#c
m = [[5,6,7,8]]
arr = transpose_matrix(m)
for i in arr:
    print(i)