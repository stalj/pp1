import random


def is_special():
    number = random.randint(1,6)
    if number == 1 or number == 6:
        special_num = True
    else:
        special_num = False
    result = f'Dice rolled: {number}\nSpecial number: {special_num}'

    return result


print(is_special())