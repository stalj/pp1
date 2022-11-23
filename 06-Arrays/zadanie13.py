array = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
sum=0
print(sum(i for i in array if not i % 2 and i != 4))
