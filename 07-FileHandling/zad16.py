with open("2022--qatar.txt", "r") as f:
    for i in f:
        a=f.readlines()
        print(a)
    with open("copy.txt", "w") as g:
        for i in a:
            g.write(i)