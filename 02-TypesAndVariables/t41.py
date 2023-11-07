def binandhex():
    num = int(input("Enter number: "))
    bina = bin(num)
    hexa = hex(num)
    return f'Binary number: {bina}\nHexadecimal number: {hexa}'


print(binandhex())