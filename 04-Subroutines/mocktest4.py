def f(number,even):
    sum = 0
    length = len(str(number))
    if even == True:
        for i in range(0, length):
            if number[i]%2 == 0:
                sum+= int(str(number[i]))
            else:
                pass

    if even == False:
         for i in range(0, length):
            if int(str(number)[i])%2 == 1:
                sum = sum +int(str(number)[i])
            else:
                pass
    
    print(sum)

f(3124,True)
f(3124,False) 
f(20576,False)
f(20576,True)
f(13115,True)

