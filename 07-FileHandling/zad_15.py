file=open('zad_15.txt','r',encoding='utf-8')

x=0
y=5

for i in file:
    print(i,end=" ")
    x=x+1
    if x==y:
        y=y+5
        if y!=35:
            z=input("aby kontynułować anciśnij enter")