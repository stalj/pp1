def in_range():
    num = int(input("Enter number: "))
    if num >= -10 and num<= 10:
        result = True
    else:
        result = False
    
    return f'Number ub range <-10, 10>: {result}'

print(in_range())