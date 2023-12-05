arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
index = 0
highest_number_of_letters = 0
highest_index = 0

while index < len(arr):
    if len(arr[index]) > highest_number_of_letters:
        highest_number_of_letters = len(arr[index])
        highest_index = index
        index += 1
    else:
        index += 1

print(arr[highest_index])