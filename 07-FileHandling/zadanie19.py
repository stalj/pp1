with open("30linesoftext.txt", "r") as f:
    lines = f.readlines()
with open("copylines.txt", "w")as m:
    for i in range(len(lines)):
        m.write(lines[i])