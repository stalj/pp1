x=[[-38, 19], [5,40],[-7,11],[29,16]]

result = []
for i in range(0, len(x)):
    largestNumber = x[i][0]
    for j in range(0, len(x[i])):
        if x[i][j] > largestNumber:
            largestNumber = x[i][j]
    result.append(largestNumber)
m=max(result)
print(max(result))

minnum=m
result1 = []
for i in range(0, len(x)):
    minnum = x[i][0]
    for j in range(0, len(x[i])):
        if x[i][j] < minnum:
            minnum = x[i][j]
    result1.append(minnum)
    mina=min(result1)
print(min(result1))

for i in range(0, len(x)):
    for j in range(0, len(x[i])):
        if x[i][j]==m:
            print("max number on pos: ", i,j)
for i in range(0, len(x)):
    for j in range(0, len(x[i])):
        if x[i][j]==mina:
            print("min number on pos: ", i,j)
            