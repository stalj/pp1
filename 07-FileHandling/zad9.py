x=[]
a=[]
with open("numbers.txt") as f:
    for i in f:
        a.append(int(i.strip("\n")))
suma=0
for i in range(0, len(a)):
    suma=suma+a[i]
print(suma)