def occurs(number, array):
    array = [15, 38, 7, 23, 14]
    if number in array:
        return True
    return False

array = [15, 38, 7, 23, 14]
number = int(input('Number: '))
print('Array:', *array, sep = ' ')
print(f'Result: number {number} appears in the array' if occurs(number, array) else f'Result: number {number} does not appear in the array')