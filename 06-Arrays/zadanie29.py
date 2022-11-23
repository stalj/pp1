array = [i for i in range(10,21)]
num = 5
more = 0
less = 0
for i in array:
    if i < num: less += 1
    if i > num: more += 1       