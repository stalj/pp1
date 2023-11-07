file = open(input("Enter file name:"))
lines = 1
for i in file:
    lines = lines +1 

print(lines-1)




file.close()