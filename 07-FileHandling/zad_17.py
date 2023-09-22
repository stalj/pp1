with open('countries.txt','r') as file1, open('copylines.txt','a') as file2:
    for i in file1:
        file2.write(i)    

