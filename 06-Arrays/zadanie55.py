import zadanie54
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
for row in matrix1:
    print(row)

print("\nTransposed Matrix:")
for row in zadanie54.transpose_matrix(matrix1):
    print(row)
matrix2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]
print("Original Matrix:")
for row in matrix2:
    print(row)

print("\nTransposed Matrix:")
for row in zadanie54.transpose_matrix(matrix2):
    print(row)

matrix3 = [5, 6, 7, 8]
print("Original Matrix:")
for row in matrix3:
    print(row)

print("\nTransposed Matrix:")
for row in zadanie54.transpose_matrix(matrix3):
    print(row)