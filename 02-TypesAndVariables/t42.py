def btod():
    binary = input("Enter binary number: ")
    result = 0
    if binary[0] == '1':
        result+= 8
    if binary[1] == '1':
        result+= 4
    if binary[2] == '1':
        result+= 2
    if binary[3] == '1':
        result+= 1
    
    return f'Binart number in decimal notation: {result}'


print(btod())