arr = [[7, 3, 7, 9, 0], [2, 9, 0, 1, 5], [3, 8, 6, 4, 7], [8, 7, 1, 1, 5]]

sum = 0

for list_number in range(len(arr)):
    sum += arr[list_number][len(arr[list_number]) - 1]

print(sum)
# print(arr[0][4] + arr[1][4] + arr[2][4] + arr[3][4])