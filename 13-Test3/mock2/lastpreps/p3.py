def f1(t):
    import re
    d={}
    pattern=r'(\w+) is (\d+)'
    a=re.findall(pattern,t)
    for key,value in a:
        d[key]=value
    sdic={}
    for key in sorted(d):
        sdic[key]=d[key]
    return sdic
def f2(d):
    sum=0
    for i in d.values():
        sum=sum+int(i)
    return sum
print(f2(f1("Mark is 24 and Ann is 27")))



print(f1("Mark is 24 and Ann is 27") )