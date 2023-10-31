def f3(t):
    import re
    a=re.findall('\d+',t)
    b=[]
    c=[]
    for i in a:
        b.append(int(i))
    
    for j in b:
        if len(str(j))==2 or len(str(j))==3:
            c.append(j)
    return sum(c)
print(f3("Przyktadowe liczby parzyste to 16, 2, 114 oraz 1014, a take 8"))