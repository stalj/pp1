with open("30linesoftext.txt", "r")as m:
    f = m.read()
with open("copy.txt", "w") as a:
    a.write(f)