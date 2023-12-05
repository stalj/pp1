arr = [34,7,19,4,21,8]
index = 0
iteration = 0
count = 0

while iteration < len(arr):
    if arr[index] % 2 == 0:
        count += 1

    index += 1
    iteration += 1

print(count)