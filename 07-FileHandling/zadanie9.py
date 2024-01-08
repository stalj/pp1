file = open("countries.txt", 'r')
count = 0
for line in file:
    count+=1
    print(f'{count}. {line}', end = '')
file.close()