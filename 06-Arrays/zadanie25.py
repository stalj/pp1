array=[15,38,7,23,14]
def occus(number,array):
    for array in array:
        if number in array:
            print(f'number {number} appears in the array')
        else:
            print(f'number {number} not appears in the array')
    return number

print(occus(23,[15,38,7,23,14]))
