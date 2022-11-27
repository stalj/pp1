import random

f=open('zad_20.txt','w')

for x in range(1,51):
    f.write(f"{random.randint(100,999)}\n")

f.close()