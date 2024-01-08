file = open('numbers.txt', 'r')
sum = 0
print('Numbers:', end = ' ')
for line in file:
    line = int(line)
    sum+=line
    print(line, end = ' ')
print()
print(f'Sum: {sum}')
file.close()
