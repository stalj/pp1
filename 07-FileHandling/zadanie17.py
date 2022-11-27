file1 = open('text.txt','r')
file2 = open('copylines.txt','w')
for line in file1:
    file2.write(f'{line}')
file1.close()
file2.close()