arr= [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
sum = 0
for i in arr:
    for j in i:
        if j%2 !=0:
            sum+=j
print(sum)