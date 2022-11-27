import re

f=open('zad_27.txt','r')

for x in range(2):
    next(f)

x=re.split("\s",f)

print(x)