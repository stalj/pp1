
def minmax(array):
    max=0
    for i in array:
        if i>max:
            max=i
    min=max
    for i in array:
        if i<min:
            min=i
    a=[]
    a.append(min)
    a.append(max)
    return(a)

x=[2,5,6,2,1,5,3,0,9,11]
print(minmax(x))