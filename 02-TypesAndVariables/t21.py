import math
height = int(input("Ender your height: "))
feet = int(height/30.48)
inches = math.ceil((height-30.48*feet)*0.39)
print(f'I am {height}cm tall, i.e {feet} feet and {inches} inches')