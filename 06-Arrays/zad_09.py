a=["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

long=int(len(a[0]))
zmienna=a[0]

for x in a:
    if int(len(x))>long:
        long=int(len(x))
print(zmienna)