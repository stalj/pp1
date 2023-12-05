array = [[True,False], [True,True], [False,False]]

for list in range(len(array)):
    for element in range(len(array[list])):
        array[list][element] = not array[list][element]

print(array)

