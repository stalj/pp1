arr = [-15, 8, -31, 47, -2, 19]
iteration = 0
index = 0

minimum = 0
maximum = 0

while iteration < len(arr):
    if arr[index] < minimum:
        minimum = arr[index]
        index += 1
        iteration += 1
    elif arr[index] > maximum:
        maximum = arr[index]
        index += 1
        iteration += 1
    else:
        index += 1
        iteration += 1

print(minimum)
print(maximum)