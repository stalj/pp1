x=[[7,3,7,9,0],[2,9,0,1,5],[3,8,6,4,7],[3,8,6,4,7],[8,7,1,1,5]]

for rows in x:
    for columns in rows:
        print(columns,end=" ")
    print()
suma=0
for i in x[4]:
    suma=suma+i
print(suma)
