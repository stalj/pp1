array = [[True,False],[True,True],[False,False]]
for i in range(int(len(array))):
    for j in range(int(len(array[0]))):
        if array[i][j] == bool("True"):
            array[i][j] = False
        else:
            array[i][j] = True 
print(array)