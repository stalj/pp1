def f5(c):
    with open("poem.txt","r") as f:
        licznik=0
        h=[]
        for a in f:
            a = a.rstrip().lower()
            h.append(a)
        for i in h:
            if c in i:
                licznik+=1
        return licznik
print(f5("m"))