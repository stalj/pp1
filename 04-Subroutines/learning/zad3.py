def f(amount_to_pay):
    a=[1,2,5]
    c=0
    x=2
    while(x>=0):
        c=amount_to_pay//a[x]
        amount_to_pay-=(c*a[x])
        if(c>0):
            print(f"{c} time {a[x]} PLN")
        x=x-1

f(5)
