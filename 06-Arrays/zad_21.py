def compare(array1,array2):
    y=0
    if len(array1)==len(array2):
        for x in range(len(array1)):
            if array1[x]==array2[y]:
                y+=1
            return("True")
                
    else:
        return("False")

a=[3,2,1]   
b=[3,2]

print(compare(a,b))