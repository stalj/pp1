from random import randint
x=randint(1,6)
y=int(input("Guess the number (1-6): "))
if y==x:
    print(True)
else:
    print(False)