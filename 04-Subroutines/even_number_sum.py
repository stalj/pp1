def f(number, even):
    i = 0
    sum = 0
    number = str(number)
    if even == 'True':
        while i < len(str(number)):
            if int(number[i])%2 == 0:
                sum += int(number[i])
            i+=1
    elif even == 'False':
        while i < len(str(number)):
            if int(number[i])%2 != 0:
                sum += int(number[i])
            i+=1
    return sum
    