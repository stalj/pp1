import random

with open("randomints.txt", "w") as f:
    for i in range(0,50):
        f.write(str(random.randint(100,999)))
        f.write("\n")