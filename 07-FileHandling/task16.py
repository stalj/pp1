file1 = open("file.txt")
text = file1.read()
file1.close()
file2 = open("copy.txt", "r")
if file2.writable():
    file2.write(text)
else: 
    print("File is not writable")
file2.close()

