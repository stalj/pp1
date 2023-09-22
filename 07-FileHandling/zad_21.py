f=open('zad_21.txt','w')

for x in range(1,11):
    f.write(f"{x} {x**2} {x**3} \n")

f.close()