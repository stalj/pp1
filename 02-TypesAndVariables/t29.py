import random
def rand():
    roll_one = random.randint(1,6)
    roll_two = random.randint(1,6)
    roll_three = random.randint(1,6)
    sum = roll_one + roll_two + roll_three
    result = f'roll one = {roll_one}\nroll two = {roll_two}\nroll three = {roll_three}\nsum = {sum}'
    return result
print(rand())