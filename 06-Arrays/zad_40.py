a=[[-38, 19], [5,40],[-7,11],[29,16]]

def max(x):
    r=int(x[0][0])
    for m in x:
        for n in m:
            if n>=r:
                r=n
    return(r,a.index(m[r]))

def min(y):
    p=int(y[0][0])
    for i in y:
        for j in i:
            if j<=p:
                p=j
    return p

print(max(a))
print(min(a))
