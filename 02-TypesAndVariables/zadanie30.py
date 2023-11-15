import random
a = random.randint(1, 6)
print(f'Dice rolled: {a}')
if a == 1 or a ==6 :
    b = True
    print(f'Special number:{b}')
else :
    b = False
    print(f'Special number: {b}')