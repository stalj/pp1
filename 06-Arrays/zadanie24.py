array = [2,3,2,5,8,1,9,8]

def get_unique_numbers(array):
    unique = [] #пустой список, если число уникальное, туда оно добавляется

    for array in array:
        if array in unique:
            continue
        else:
            unique.append(array)
    return unique

print(get_unique_numbers(array))