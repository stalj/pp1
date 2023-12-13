# f = open("countries.txt")
# for line in f:
#      print(line, end="")
# f.close()

with open("countries.txt") as something:
    for line in something:
        print(line, end="")