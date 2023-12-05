arr = [15, 8, 31, 47, 2, 19]
reversed_arr = []

index = len(arr) - 1
iteration = 0

# Shit doesn't work
# while iteration < len(arr):
#     reversed_arr += arr[index]
#     index -= 1
#     iteration += 1

# Both work
arr.reverse()
reversed_arr = list(arr)

reversed_arr = arr[::-1]

print(reversed_arr)

