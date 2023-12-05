arr = [15, 8, 31, 47, 2, 19]
sum = 0

for index in arr:
    sum += index

mean = sum / len(arr)

print(round(mean, 2))