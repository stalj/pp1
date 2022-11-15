a=[[True,False],[True,True],[False,False]]

for x in a:
    for y in x:
        if y==True:
            print(False, end=" ")
        elif y==False:
            print(True, end=" ")
