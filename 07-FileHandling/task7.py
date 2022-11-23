file = open('countries.txt','r')
counter = 1
for line in file:
     print(counter, line, end="")
     counter = counter + 1

file.close()