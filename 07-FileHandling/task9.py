file = open('numbers.txt','r')
sum = 0
for line in file:
    sum = sum + int(line)

file.close()
print(sum)
