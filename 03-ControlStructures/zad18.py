a=[1,2,5]
b=int(input("Enter the amount: "))
c=0
x=2
while(x>=0):
    c=b//a[x]
    b-=(c*a[x])
    if(c>0):
        print(f"{c} time {a[x]} PLN")
    x=x-1