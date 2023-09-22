x=1

for z in range(30):
    if x%3==0 and x%5!=0:
        print("TRZY")
    if x%5==0 and x%3!=0:
        print("PIĘĆ")
    if x%3!=0 and x%5!=0:
        print(x)
    if x%3==0 and x%5==0:
        print("BINGO")
    
    x+=1

