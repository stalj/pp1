for num in range(1,31):
    if num % 3 == 0 and num % 5 == 0:
        print(end=" BINGO ")
    elif num % 3 == 0:
        print(end=" THREE ")
    elif num % 5 == 0:
        print(end=" FIVE ")
    else:
        print(str(num),end=" ")

