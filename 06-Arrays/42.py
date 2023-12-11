import random as r
def rand_elem(array):
    return array[r.randint(0,len(array))]


arr = [7, 3, 8, 5, 2]

print(rand_elem(arr))