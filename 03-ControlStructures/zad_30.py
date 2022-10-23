a = int(input("Podaj ilość liczb pierwszych: "))
count=0
i=2
while(count!=a):
    if i==2 or i==3 or i==5:
        print(i)
        count+=1
    elif i%2!=0 and i%3!=0 and i%5!=0:
        print(i)
        count+=1
    i+=1
