arr1 = [2, 3, 2, 5, 8, 1, 9, 8]

# counts numbers that DO NOT REPEAT
arr2 = [num for num in arr1 if arr1.count(num) == 1]

# SET Clears the list of all duplicates, and turns the var into a set
# LIST converts the set back to a list
arr2 = list(set(arr2))

print(arr2)