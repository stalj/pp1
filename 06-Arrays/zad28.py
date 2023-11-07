def median(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] < array[j]:
                array[j],array[i] = array[i],array[j]
    return array

listToSort = [22,11,23,1,100,24,3,101,2,4]
print(median(listToSort))