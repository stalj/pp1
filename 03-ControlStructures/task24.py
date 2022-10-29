x = 8
for i in range(0, x):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")

for i in range(x , 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")