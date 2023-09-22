def f(a):
    i=a[0]
    for x in a:
        if x>i:
            i=x
    j=a[0]
    for y in a:
        if y<j:
            j=y
    diff=i-j
    return diff

b=[5,1,9,6,1]
print(f(b))