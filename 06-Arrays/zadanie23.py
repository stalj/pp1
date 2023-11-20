arr = [-15, 8, -31, 47, -2, 19]
maximum = arr[0]
minimum = arr[0]
for i in arr:
    if i > maximum:
        maximum = i
for i in arr:
    if i < minimum:
        minimum = i
print(f'Max: {maximum}')
print(f'Min: {minimum}')