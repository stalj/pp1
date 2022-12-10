file = open('countries.txt', 'r', encoding='utf-8')
for line in file:
    print(line, end="")    
file.close()