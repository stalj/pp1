def sum(n):
    if n==0:
        return 0
    else:
        return n + sum(n-1)

x=10
print (f'suma liczb z przedziału <1;{x}> jest róna {sum(x)}')