a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))
s = (a+b+c)/2
area = (s*(s - a)*(s - b)*(s - c))**(1/2)
print(f'Triangle area: {area}')
print(f'Triangle cimcumference: {a+b+c}')