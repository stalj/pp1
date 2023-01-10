def f(a,b):
    import re
    x=open("copy.txt","r",encoding="utf-8").read()
    y=re.findall(rf'\b[{a}]\w+[{b}]\b', x)
    sum=0
    for i in y:
        sum+=1
    print(sum)

f("p","j")