array = [3,9,2],[2,4,5],[7,1,6],[0,4,8]
sum = 0
for i in range(int(len(array))):
    for j in range(int(len(array[0]))):
        sum = sum + int(array[i][j])
    
print(sum)
    