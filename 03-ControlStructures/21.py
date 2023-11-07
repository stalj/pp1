number1 = int(input("enter first number: "))
number2 = int(input("enter second number: "))

if number1 > number2:
    print(f"Numbers in ascending order: {number2}, {number1}")
elif number2 > number1:
    print(f"Numbers in ascending order: {number1}, {number2}")
else:
    print(f"Both {number1} and {number2} are equal.")