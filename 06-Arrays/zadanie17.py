arr = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(arr)):
    arr[i][i]+=1
    print(*arr[i], sep = ' ')