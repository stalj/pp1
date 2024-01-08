a = (input('Enter binary number: '))
if len(a) <= 4 :
    b = int(a[0])
    c = int(a[1])
    d = int(a[2])
    e = int(a[3])
    print(f'Binary number in decimal notation: {(b*2**3) + (c*2**2) + (d*2**1) + (e*2**0)}')
else :
    print("You can only enter four-digit number!")