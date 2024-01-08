array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

smallest_value = float('inf')
largest_value = float('-inf')
smallest_row = largest_row = smallest_col = largest_col = None

for i in range(len(array)):
    for j in range(len(array[i])):
        current_value = array[i][j]

        if current_value < smallest_value:
            smallest_value = current_value
            smallest_row, smallest_col = i, j

        if current_value > largest_value:
            largest_value = current_value
            largest_row, largest_col = i, j

print(f"The smallest value is {smallest_value}, located at row {smallest_row} and column {smallest_col}.")
print(f"The largest value is {largest_value}, located at row {largest_row} and column {largest_col}.")
