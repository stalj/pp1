a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
if (a >= 0 or b >= 0):
    print(f'At least one of entered numbers {a} and {b} is not negative')
else:
    print(f'Both of numbers are negative')