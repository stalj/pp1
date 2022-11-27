def f(array1,array2):
    i=0
    for x in range(len(array2)):
        if x==array1[i]:
            i+=1
        return True
    return False

        

a=[5,4,3,1]
b=[6,5,4,3,2]

print(f(a,b))