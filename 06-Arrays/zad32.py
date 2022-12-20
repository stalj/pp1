
x=[2,3,4,5,6]

def ats(arr):

    y=[]
    for i in arr:
        y.append(str(i))
    s=",".join(y)
    return(s)
print(ats(x))