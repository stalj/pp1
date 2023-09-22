f1=open('shoppinglist.txt','w')
f2=open('GrainsAndBread.txt','r')
f3=open('MeatAndFish.txt','r')

f1.write(f2.read())
f1.write(f3.read())