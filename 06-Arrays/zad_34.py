def f(a,b):
    for i in a:
        if i not in b:
            return False
    return True
        

a1=[5,4,3,1]
a2=[6,5,4,3,2]

print(f(a1,a2))
