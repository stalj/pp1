array = [1,2,3,4,5]
print(array[1:]) #or array[0] = array[0]-1
print(array[-1]*4)
print(array[int(len(array)/2)]*2)

for i in range(0,len(array)):
    array[i] +=3
    print(array[i], end = ' ')