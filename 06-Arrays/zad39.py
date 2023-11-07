array=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for row in range(0,len(array)):
    i=1
    if row==0:
        for column in range(0,len(array)):
            array[row][column]=array[row][column]+i
            i=i+1
    i=2
    if row==1:
        for column in range(0,len(array)):
            array[row][column]=array[row][column]+i
            i=i+2
    i=3
    if row==2:
        for column in range(0,len(array)):
            array[row][column]=array[row][column]+i
            i=i+3
    i=4
    if row==3:
        for column in range(0,len(array)):
            array[row][column]=array[row][column]+i
            i=i+4
    i=5
    if row==4:
        for column in range(0,len(array)):
            array[row][column]=array[row][column]+i
            i=i+5
for i in array:
    print(i)
    print()