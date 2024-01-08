height_in_cm = float(input("Enter your height in centimeters: "))

height_in_inches = height_in_cm / 2.54
height_in_feet = int(height_in_inches // 12)
remaining_inches = int(height_in_inches % 12)

print(f"I am {height_in_cm}cm tall, i.e. {height_in_feet} feet and {remaining_inches} inches.")
