x=[[1, 2, 3],[3, 6, 7],[7 ,5, 4]]
def zamiana(arr):
    y=[]
    for i in arr:
        y.extend(i)
    return(y)

print(zamiana(x))

a=[[2,3],[1,5]]
b=[[5,0,3,7,5],[9,0,9,1,2]]

print(zamiana(a))
print(zamiana(b))