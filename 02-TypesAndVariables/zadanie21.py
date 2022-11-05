from random import randint

roll = randint(1,6)
guess = int(input('Your guess is : '))
if roll == guess:
    print("True")
else:
    print('False')
print('The number was: ' + str(roll))