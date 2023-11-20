arr=[[True,False],[True,True],[False,False]]
print(arr)
for i in range(len(arr)):
    for j in range(len(arr[0])):
        arr[i][j] = not arr[i][j] 
print(arr)