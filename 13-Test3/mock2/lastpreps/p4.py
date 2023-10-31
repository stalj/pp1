def f(d):
    parking=[]
    for key,value in d:
        if value=="in":
            parking.append(key)
        elif value=="out":
            parking.remove(key)
    return sorted(parking)


cars=[["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
["BA111","in"],["BA123","out"],["KR234","in"]]

print(f(cars))