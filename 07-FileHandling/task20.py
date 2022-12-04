import random
file = open("randomint.txt", "w")
for i in range(50):
    i = random.randint(100,1000)
    i = str(i) + "\n"
    file.write(i)
file.close()