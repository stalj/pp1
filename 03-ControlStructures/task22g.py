for i in range(1,31):
    if  i%3 == 0 and i%5 ==0:
        print(i, "BINGO ", end= "")
    elif i%5 == 0:
        print(i, "FIVE ", end= "")
    elif i%3 == 0:
        print(i,"THREE ", end= "")
    else:
        print(i ," ", end= "")