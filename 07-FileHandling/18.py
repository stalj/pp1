# Open text as f, from there open other text as c, write whatever is in f to c
with open("some_file.txt") as f:
    with open("copy_file.txt", "w") as c:
        c.write(f.read())