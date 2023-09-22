def f(t):
    a=[]
    for x in t:
        if x[1]=="in":
            a.append(x[0])
        elif x[1]=="out":
            a.remove(x[0])
    a.sort()
    return a

cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
["BA111","in"],["BA123","out"],["KR234","in"]]
print(f(cars)) 
