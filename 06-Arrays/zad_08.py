a=[-15, 8, -31, 47, -2, 19]

def max(a):
    x=0
    for i in a:
        if i>x:
            x=i
    print(x)

def min(a):
    x=0
    for i in a:
        if i<x:
            x=i
    print(x)

max(a)
min(a)