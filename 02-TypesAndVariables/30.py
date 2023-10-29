import random

dice = random.randint(1, 6)

if dice == 1 or dice == 6:
    special_something = True
else:
    special_something = False

print(f"Dice rolled: {dice}\nSpecial number: {special_something}")