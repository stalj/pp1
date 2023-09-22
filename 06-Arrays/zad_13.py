a=[[3,9,2],[2,4,5],[7,1,6],[0,4,8]]

sum=0

for x in a:
    for y in x:
        if y%2==0:
            sum+=y

print(sum)