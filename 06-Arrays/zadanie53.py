def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
def display(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = ' ')
        print()
display(identity_matrix(5))