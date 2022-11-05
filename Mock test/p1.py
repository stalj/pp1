def f(card_number):
    z=str(card_number)
    y=""
    for x in range(0,16):
        if (x==0 or x==1 or x==12 or x==13 or x==14 or x==15):
            y=y+z[x]
        else:
            y=y+"*"
    return (y)
