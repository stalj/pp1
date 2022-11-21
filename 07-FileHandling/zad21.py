a=[]
with open("powers.txt", "w") as f:
    for i in range(1,11):
        f.write(str(i))
        f.write(",")
        f.write(str(i**2))
        f.write(",")
        f.write(str(i**3))
        f.write("\n")