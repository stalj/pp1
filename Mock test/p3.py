def f(a):
    if a%5==0:
        x=a//5
        y1=0   
    else:
        x=a//5
        y1=a-x*5
    if y1%2==0:
        y2=y1//2
        y5=0
        y4=0
    else:
        y2=y1//2
        y5=y1-y2*2
    if y5!=0:
        y4=y5//1
    return f"to jest {x+y2+y4} monet"
