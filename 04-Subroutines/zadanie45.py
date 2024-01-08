def f(experession):
    experession = str(experession)
    a = 0
    result = int(experession[0])
    for i in experession:
        if i == '+':
            result += int(experession[a+1])
        if i == '-':
            result -= int(experession[a+1])
        a +=1
    return result

if __name__== '__main__':
    print(f('2+3'))
    print(f('3+8+1'))
    print(f('2+3-4+5-0'))
