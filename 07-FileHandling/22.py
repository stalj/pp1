import random as r

with open("rand_numbers","w") as f:
    for number in range(1,51):
        f.write(str(r.randint(100,999)) + "\n")