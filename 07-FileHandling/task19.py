file = open("intigers.txt", "w")
for i in range(1,51):
    i = str(i) + "\n"
    file.write(i)
file.close()