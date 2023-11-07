import random 

def challange():
    number = int(input("Guess number: "))
    randnum = random.randint(1,6)
    if randnum == number:
        result = True
    else:
        result = False

    return result


print(challange())