array = [2, 3, 7, 5, 4]

print(f"the array: {array}")
print(f"number of elements: {len(array)}")
print(f"first value: {array[0]}")
print(f"second value: {array[1]}")
print(f"last value: {array[-1]}")
print(f"last but one value: {array[-2]}")
print(f"sum of the first and last value: {array[0] + array[-1]}")
print(f"middle value: {array[len(array) // 2]}")

for i in array:
    print(i, end = " ")

print()

for i in range(len(array) // 2 + len(array) % 2):
    print(array[i], end = " ")
