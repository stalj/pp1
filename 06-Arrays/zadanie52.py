arr = [[7, 5, 3, 8, 1],
[6, 8, 9, 2, 1],
[10, 4, 6, 1, 5]]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end = ' ')
    print()
for i in range(len(arr)):
    arr[i][0], arr[i][-1] = arr[i][-1], arr[i][0]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end = ' ')
    print()