def nonnegative():
    num1 = int(input("Enter numner 1: "))
    num2 = int(input("Enter number 2: "))
    if num1 > 0 or num2 > 0:
        result = f'At least one of entered numbers {num1} and {num2} is not negative'
    else:
        result = f"{num1} and {num2} are negative numbers!!!!" 

    return result


print(nonnegative())