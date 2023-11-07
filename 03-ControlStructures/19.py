sum = 0

for iteration in range (1,11):
    if iteration % 2 == 0:
        print(iteration)
        sum += iteration
    else:
        continue

print("")
print(sum)