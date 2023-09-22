def f(n):
    i=0
    j=1
    for x in range(2,n+1):
        if x%2==0:
            i+=j
        else:
            j+=i
    if n%2==0:
        return(j)
    else:
        return(i)