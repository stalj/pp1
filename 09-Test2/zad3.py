def f(array2D):
    l=[]
    sum=0
    for i in array2D:
        h=len(i)
    for j in range(h):
        for i in range(len(array2D)):
            sum+=array2D[i][j]
        l.append(sum)
        sum=0
    print(l)
f([ [3,6,2,7], [9,5,4,0], [2,8,0,9] ]) 
