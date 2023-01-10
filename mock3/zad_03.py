def f1(t):
    import re
    x=re.findall(r"[A-Z][a-z]+",t)
    y=re.findall(r"\d+",t)
    z={}
    for i in range(len(x)):
        z[x[i]]=y[i]
    print(dict(sorted(z.items())))

def f2(n):
    import re
    sum=0
    x=re.findall(r"\d+",n)
    for y in x:
        sum+=int(y)
    print(sum)



f1("Mark is 24 and Anna is 27")
f2("Peter is 11, Barbara is 7 and their grandfather John is 103!!")