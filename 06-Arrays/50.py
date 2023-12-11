arr = [[-38, 19],
       [5,40],
       [-7,11],
       [29,16]]

mini = 0
maxi = 0

mini_row = 0
mini_column = 0

maxi_row = 0
maxi_column = 0

for list_num in range(len(arr)):
    for num in arr[list_num]:
        if num < mini:
            mini = num
            mini_row = list_num
            mini_column = arr[list_num].index(mini)
        elif num > maxi:
            maxi = num
            maxi_row = list_num
            maxi_column = arr[list_num].index(maxi)

print(f"{mini}, [{mini_row}], [{mini_column}]")
print(f"{maxi}, [{maxi_row}], [{maxi_column}]")

