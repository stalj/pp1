file=open('zad_15.txt','r',encoding='utf-8')
y="\n"
for z in file:
    if y=="\n":
        for x in range(5):
            print(file.readline())
        y=input("")