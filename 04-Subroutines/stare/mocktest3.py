def f(amount):
    rem = amount % 5
    zl5 = (amount - rem)/5
    rem = amount % 2 
    zl2 = (amount - rem)/2
    zl1 = rem

    print(int(zl5 + zl2 + zl1))
    


f(8)
f(2)
f(0)

#jest źle:)
