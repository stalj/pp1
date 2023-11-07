array = [1,2,3,4,5]
#a.	subtract one from the first element of the array
array[0] = array[0] - 1
print(array)

#b.	increase the last array element by 4
array[4] = array[4] + 4
print(array)
#c.	multiple the middle array element by 2
array[int(len(array)/2 )] = array[int(len(array)/2)] *2
print(array)
#d.	adds 3 to each value of the array (use a loop statement)
for i in range(int(len(array))):
    array[i] = array[i] + 3
    print(array[i] , end = ' ')