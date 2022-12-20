x=[[1,2,3],[5,6,7], [4,7,1], [7,8,9], [4,2,1]]
for rows in x:
    for columns in rows:
        print(columns,end=" ")
    print()
suma=0
for i in range(3):
    t = x[0][i]
    x[0][i] = x[5-1][i]
    x[5-1][i] = t

print()
print()
print()

for rows in x:
    for columns in rows:
        print(columns,end=" ")
    print()
suma=0