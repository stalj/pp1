

def zamiana(array, n, m):
    rows = n
    for i in range(n):
      t = array[0][i]
      array[0][i] = array[rows-1][i]
      array[rows-1][i] = t
 
array = [[-38, 19], [5,40],[-7,11],[29,16]]
n = 4
m = 4
print(zamiana(array, n, m))

for i in range(n):
    for j in range(m):
        print(array[i][j], end = " ")
    print(" ")