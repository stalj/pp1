array = [
    [2,5,4],
    [9,0,3]
    ]

print(f'a) {array}')
print()
print(len(array), len(array[0])) #size of the array 
#print(f'b)' len(array))
print(array[0][1])
print(array[1][2])

print(array[1])

for i in array:
    for j in i:
        print(j, end =' ')
    print()

print(array[0][-1],array[1][-1])#jak znajleżć 