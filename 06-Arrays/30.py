arr1 = [7, 6, 5, 4, 3, 2, 1]
arr2 = [4,36,12,28,9,44,5]


def bubblesort(arr):
    iterations = len(arr) - 1
    loops = len(arr) - 1
    index = 0
    aux = 0

    while loops != 0:
        while index < iterations:
            #      1              2
            if arr[index] > arr[index + 1]:
                aux = arr[index]
                arr[index] = arr[index + 1]
                arr[index + 1] = aux
                index += 1
            else:
                index += 1
        index = 0
        loops -= 1
        iterations -= 1
    return arr

print(bubblesort(arr2))
