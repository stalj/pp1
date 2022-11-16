def f(x,y,z):
    if x > y and y > z and x > z:
        print(x-z)
    elif x > y and y < z and x > z:
        print(x-y)
    elif y > x and x < z and z < y:
        print(y-x)
    elif y > x and x > z and y > z:
        print(y-z)
    elif z > x and x < z and y < x:
        print(z-y)
    else:
        print(z-x)

f(17,15,19)
f(29,14,19)
    