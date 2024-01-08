first_name = str(input('Enter first person name: '))
first_age = int(input('Enter fist person age: '))
second_name = str(input('Enter second person name: '))
second_age = int(input('Enter second person age: '))
if first_age >= 18 and second_age >= 18:
    print(f'Both {first_name} and {second_name} are adults.')
else: 
    print("At least one of them isn't adult.")