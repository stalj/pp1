array = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
longest=len(array[0])
zmienna=array[0]

for x in array:
    if (len(x)>longest):
        longest=len(x)
        zmienna=x

print(zmienna)