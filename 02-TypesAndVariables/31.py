import random

dice = random.randint(1, 6)
print(dice)

guess = int(input("Thine guess, peasant?: "))

if guess == dice:
    print("...What? You want a medal or something?")
else:
    print("PHA!!! You absolute FOOL!! Thou shalt remain a meansly PEASANT, just as your father!!!")