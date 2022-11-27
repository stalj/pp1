import re

f1=open('zad_15.txt','r')
f2=open('words.txt','w')
a=re.split("\s",f1,10)

for x in a:
    if len(x)>=6:
        f2.write(f"{x}\n")

