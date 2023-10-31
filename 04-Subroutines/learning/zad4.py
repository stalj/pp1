def f(number, even):
    s=0
    if even==False:
        while number>0:
            n1=number%10
            if(n1%2==1):
                s=s+n1
            number=number//10
        print(s)
    elif even==True:
        while number>0:
            n1=number%10
            if(n1%2==0):
                s=s+n1
            number=number//10
        print(s)
f(3124, True)
f(3124,False)
f(20576,False)
f(20576,True)
f(13115,True)