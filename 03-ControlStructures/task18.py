amount=int(input("Enter the amount in PLN: "))
if amount%5 == 0:
    zl5=amount//5
    zl2=0
    zl1=0
    print(f"5zl-{zl5}")
    print(f"2zl-{zl2}")
    print(f"1zl-{zl1}")
elif amount%5==2 or amount%5==4:
    zl5=amount//5
    zl2=(amount-5*zl5)//2
    zl1=0
    print(f"5zl-{zl5}")
    print(f"2zl-{zl2}")
    print(f"1zl-{zl1}")
else:
    zl5=amount//5
    zl2=(amount-5*zl5)//2
    zl1=1
    print(f"5zl-{zl5}")
    print(f"2zl-{zl2}")
    print(f"1zl-{zl1}")