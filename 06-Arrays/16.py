array = [[3,9,2], [2,4,5], [7,1,6], [0,4,8]]

sum = 0

for iteration in array:
    for thing in iteration:
        if thing % 2 != 0:
            sum += thing


print(sum)
