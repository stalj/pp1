def cBMI():
    height = float(input("Enter your height: "))
    weight = float(input("Enter your weight: "))
    bmiindex = weight/(height/100)**2.0
    if bmiindex >=18.5 and bmiindex <= 24.99:
        correct_weight = True
    else:
        correct_weight = False
    result = f'Your BMI index: {bmiindex}\nCorrect weight: {correct_weight}'
    
    return result





print(cBMI())