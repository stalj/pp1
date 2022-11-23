def prarr(arr):
    if len(arr)==0:
        return
    print(*arr[0])
    prarr(arr[1:])
    
n=int(input("n="))
m=int(input("m="))
 
arr=[[i*j for i in range(1,n+1)] for j in range(1,m+1)]
prarr(arr)