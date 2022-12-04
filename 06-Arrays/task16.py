array = [15, 8, 31, 47, 2, 19]
print(f"existed array: {array}")
#array.reverse()
print("reverse array: ", end = " ")
for i in range(int(len(array)-1), -1, -1):
    print(array[i], end = " ")
