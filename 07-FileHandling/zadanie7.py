file = open('countries.txt','r',encoding='utf-8' )
i=1

for line in file:
     print(i,line, end="")
     i+=1 # or i=i+1
