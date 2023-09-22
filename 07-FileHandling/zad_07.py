file = open('countries.txt','r')
i=1
for line in file:
     print(i,line, end="")
     i+=1
     