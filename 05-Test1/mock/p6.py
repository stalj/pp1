def f(number, even):
    number = str(number)
    sum = 0
    for i in number:
        i = int(i)
        if even == True:
            if i%2 ==0:
                sum += i
        elif even == False:
            if i%2 != 0:
                sum += i
    return sum

if __name__ == '__main__':
    print(f(3124, True))
    print(f(3124, False))
    print(f(20576, True))
    print(f(20576, False))
    print(f(13115, True))