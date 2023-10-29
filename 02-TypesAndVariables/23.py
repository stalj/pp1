import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

p = 0.5 * (a+b+c)
# area = math.sqrt(p*(p-a)*(p-b)*(p-c))
root = math.sqrt((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c))
area = root/4

circumference = a+b+c

print(f"Triangle area: {area}\nTriangle circumference: {circumference}")