arr = [[7, 5, 3, 8, 1],
[6, 8, 9, 2, 1],
[10, 4, 6, 1, 5]]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end = ' ')
    print()
arr[0], arr[-1] = arr[-1], arr[0]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end = ' ')
    print()