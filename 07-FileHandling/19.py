# Same shit, 'cept we create a list, and from there, we write each line into the c file
with open("some_file.txt") as f:
    with open("copy_file.txt", "w") as c:
        lines = f.readlines()
        for line in lines:
            c.write(line)