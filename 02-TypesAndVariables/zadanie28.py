a = float(input('Enter your height in cm: '))
b = float(input('Enter your weight in kg: '))
d = round(b/(a/100)**2, 2)
print(f'Your BMI index:{d}')
if (d <= 24.9 and d >= 18.5 ) :
    c = True
    print(f'Correct weight: {c}')
else :
    c = False
    print(f'Correct weight: {c}')
