import re
with open('MeatAndFish.txt','r') as file:

    zmienna = re.findall('\w+',file.read())
        
    x=0
    for i in zmienna:
        if len(zmienna[x])>=6:
            print(zmienna[x])
        x=x+1