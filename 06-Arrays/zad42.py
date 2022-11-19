x=[[1,2,3],[5,6,7], [4,7,1], [7,8,9], [4,2,1]]
for rows in x:
    for columns in rows:
        print(columns,end=" ")
    print()
suma=0
for i in range(5):
    t = x[i][0]
    x[i][0] = x[i][3-1]
    x[i][3-1] = t

print()
print()
print()

for rows in x:
    for columns in rows:
        print(columns,end=" ")
    print()
suma=0