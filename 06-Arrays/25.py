arr = [15, 8, 31, 47, 2, 19]
index = 0
sum = 0

while index < len(arr):
    sum += arr[index]
    index += 1

mean = sum / len(arr)

print(round(mean, 2))