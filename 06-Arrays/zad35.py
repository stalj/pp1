x=[1,2,3,4,5,6,7,8,9,10]

def rand_elem(array):
    import random
    d=random.randint(0,10)
    for i in range (1,d):
        print(random.randint(array[0],array[-1]))
print(rand_elem(x))