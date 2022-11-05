human_age=int(input('Enter the dogs age in human years:'))
if human_age < 0:
    print('Must be positive')
elif human_age <=2:
    dogs_age=human_age*10.5
else:
    dogs_age = 2*10.5 + (human_age - 2)*4
print("The dog's age in dog's years is", dogs_age)
