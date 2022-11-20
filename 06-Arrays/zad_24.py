def unique(array):
    for x in range(len(array)):
        for y in range(len(array)):
            if array[x]!=array[y]:
                return array[y]

a=[2,1,2,3,4,3,5,3]

print(unique(a))