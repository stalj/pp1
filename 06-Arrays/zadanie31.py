
def f(array):
     return [int(i) for i in array if i % 2 == 0], [int(i) for i in array if i % 2 != 0]

print(f([1,2,6,3,5]))


        