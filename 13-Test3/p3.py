def f3(t):
    import re
    p=r'(\w+) is (\d+)'
    matches=re.findall(p,t)
    print(matches)
    dic={}
    sdic={}
    for key, value in matches:
        dic[key]=value
    for key in sorted(dic):
        sdic[key]=dic[key]
    return sdic
def f2(d):
    sum=0
    for d in d.values():
        sum=sum+int(d)
    return sum
#print(f3("Mark is 24 and Ann is 27"))
#print(f3("Peter is 11, Barbara is 7 and their grandfather John is 103!!"))
print(f2(f3("Mark is 24 and Ann is 27")))
print(f2(f3("Peter is 11, Barbara is 7 and their grandfather John is 103!!")))