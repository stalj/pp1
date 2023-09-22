def power(x,n):
    y=x
    while n>1:
        x*=y
        n-=1
    return x

print(power(5,3))