import math

height = 190

feet = math.floor(height/30.48)
inches = round((height/30.48 - feet) * 12)

print(f"I am {height}cm tall, in wrong units it's: {feet} feet and {inches} inches.")
