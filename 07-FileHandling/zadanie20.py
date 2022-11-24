import random

file = open('z20.txt', 'w')

for i in range(50):
    i=random.randint(100,999)

    file.write(f'{i}\n' )
file.close()
