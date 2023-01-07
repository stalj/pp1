def f(cars):
    parking=[]
    for key,value in cars:
        if value=="in":
            parking.append(key)
        elif value=="out":
            parking.remove(key)
    print(sorted(parking))
cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
["BA111","in"],["BA123","out"],["KR234","in"]]

print(f(cars))