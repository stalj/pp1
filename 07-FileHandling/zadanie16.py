with open('text.txt', 'r' , encoding='utf-8') as firstfile, open('copy.txt', 'a') as secondfile:
    for line in firstfile:
        secondfile.write(line)

