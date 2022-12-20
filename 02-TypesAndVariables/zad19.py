height=int(input("Enter your height in cm: "))
height=height/100
weight=int(input("Enter your weight in kg:  "))
bmi=weight/height**2
print('Your BMI index is: {:.2f}'.format(bmi))
