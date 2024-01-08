a = 1
array = []
while a <=5:
    b = '*'
    array.append(b)
    print(*array, sep=" ")
    b = b +'*'
    a = a+1

while a > 5 and a <= 9:
        c = '*'
        array.remove(c)
        print(*array, sep=" ")
        c = c + '*'
        a = a+1
