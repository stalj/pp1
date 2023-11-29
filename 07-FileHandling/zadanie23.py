with open("integers_power.txt", "w")as f:
    for i in range(1, 11):
        f.write(str(i)+","+str(i**2)+","+str(i**3)+"\n")