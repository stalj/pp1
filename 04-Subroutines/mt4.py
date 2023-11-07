def f(number, even):
    length = len(str(number))
    sum = 0
    if even == True:
        for i in range(0,length):
            if int(str(number)[i]) % 2 == 0:
                sum += int(str(number)[i])
            else:
                pass

    if even == False:
        for i in range(0,length):
            if int(str(number)[i]) % 2 != 0:
                sum += int(str(number)[i])
            else:
                pass
    print(sum)

f(3124,True)        
