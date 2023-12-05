array = [[True,False], [True,True], [False,False]]

for iteration in array:
    for thing in iteration:
        if thing == False:
            thing = True
        elif thing == True:
            thing = False

print(array)

