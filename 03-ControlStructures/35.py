number = 1
while number <= 30:
    if number % 3 == 0 and number % 5 == 0:
        print("BINGO")
        number += 1
    elif number % 5 == 0:
        print("FIVE")
        number += 1
    elif number % 3 == 0:
        print("THREE")
        number += 1
    else:
        print(number)
        number += 1
