def function(amount_to_pay):
    amount = amount_to_pay
    number = 0

    while amount - 5 >= 0:
        number += 1
        amount -= 5
    while amount - 2 >= 0:
        number += 1
        amount -= 2
    while amount - 1 >= 0:
        number += 1
        amount -= 1

    return number

print(function(0))