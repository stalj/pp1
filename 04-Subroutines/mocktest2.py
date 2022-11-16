def f(binary_number):
    length = len(binary_number)
    binary= None
    for i in range(0,length):
        if binary_number[i] == "0" or binary_number[i] == "1":
            pass
        else:
            binary = False
            print(binary)
            return False
    binary = True
    print(binary)

f("101101")
f("1311a10100")
