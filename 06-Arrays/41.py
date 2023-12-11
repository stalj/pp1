arr = [[7,3,8,5,2], [2,5,8,3,7]]

var = True

for i in arr:
    for j in arr[0]:
        if j not in arr[1]:
            var = False

print(var)