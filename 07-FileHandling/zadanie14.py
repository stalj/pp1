lines = 0
file = input('name:')

for line in open(file, 'r'):
    lines += 1

print("Lines:", lines)