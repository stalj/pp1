
import mymath
import random

x=mymath.read_number()
y=mymath.generate_number()

if x==y:
    print("Wygrałeś!")
else:
    print(f'Przegrałeś. To jest {y}')