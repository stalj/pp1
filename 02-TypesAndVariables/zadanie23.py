import math
a=float(input('First side:'))
b=float(input('Second side:'))
c=float(input('Third side:'))
s=(a+b+c)/2
if ((a + b) > c and (a + c) > b and (b + c) > a) :
    print(f'Triangle area: {round(math.sqrt(s*(s-a)*(s-b)*(s-c)), 2)}')
    print(f'Triangle circumference: {a+b+c}')
else :
    print("Such triangle doesn't exist")