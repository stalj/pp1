def identity_matrix(n):
    a=[[]]
    for x in range(0,n):
        for y in range(0,n):
            if x==y:
                a[x][y]=1
            else:
                a[x][y]=0
    return a

print(identity_matrix(3))