def f(number,even):
    y=str(number)
    x1=0
    x2=0
    if even==True:
        for x in y:
            if int(x)%2==0:
                x1+=int(x)
        return x1
    else:
        for x in y:
            if int(x)%2!=0:
                x2+=int(x)
        return x2
