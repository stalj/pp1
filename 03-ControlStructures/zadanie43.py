i = 0
array=[0, 1]
for i in range (2, 20):
    next_number = array[-1] + array[-2]
    array.append(next_number)

print(*array, sep = " ")
