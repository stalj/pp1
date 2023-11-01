def is_even():
    number = int(input("Enter number: "))
    if number%2 == 0:
        check = True
    else:
        check = False
    
    return f"Number is even: {check}"


print(is_even())