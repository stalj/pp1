file = open("numbers.txt", "r")

sum = 0
for iteration in file:
    sum += int(iteration)

print(sum)