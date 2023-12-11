arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
#           0           1           2           3           4
loops = len(arr)
list_number = 0
mult = 1

while loops != 0:
    for i in range(5):
        arr[list_number][i] = (i + 1) * mult
    loops -= 1
    list_number += 1
    mult += 1


print(arr)


