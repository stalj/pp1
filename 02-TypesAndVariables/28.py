height = float(input("Enter your height in cm: "))
height /= 100
weight = float(input("Enter your weight in kg: "))

bmi = round(weight/height**2, 1)

if 18.5 <= bmi <= 25:
    bmi_correctness = True
else:
    bmi_correctness = False
print(f"Your BMI index: {bmi}")
print(f"Correct weight: {bmi_correctness}")