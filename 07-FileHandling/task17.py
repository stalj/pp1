file1 = open("file.txt")
file2 = open("copylines.txt", "w")
text = ""
for i in file1:
    text = text + i 
file1.close()
file2.write(text)