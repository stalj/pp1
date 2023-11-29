import random
with open("integers_random.txt", "w")as f:
    for i in range(50):
        f.write(str(random.randint(100,999))+"\n")