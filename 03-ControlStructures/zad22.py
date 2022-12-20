for i in range(1,31):
    if i%3!=0 and i%5!=0:
        print(i)
    elif i%3==0:
        if i%5!=0:
            print("THREE")
        else:
            print("BINGO")
    elif i%5==0:
        if i%3!=0:
            print("FIVE")
        else:
            print("bingo")
