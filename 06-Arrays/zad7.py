arr7 = [1, 2, 3, 4, 5]

# arr7[0] = arr7[0] - 1
arr7[0] -= 1

# arr7[-1] = arr7[-1] + 4
arr7[-1] += 4

# arr7[len(arr7) // 2] = arr7[len(arr7) // 2] * 2
arr7[len(arr7) // 2] *= 2

for i in range(len(arr7)):
    arr7[i] += 3

print(arr7)