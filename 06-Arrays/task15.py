array = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(int(len(array))):
    for j in range(int(len(array[0]))):
        if i == j :
            array[i][j] = 1
        else:
            array[i][j]
        
for i in range(int(len(array))):
    for j in range(int(len(array[0]))):
        if j ==2:
             print(array[i][j], end = " ")
             print()
        else:
            print(array[i][j], end = " ")
        