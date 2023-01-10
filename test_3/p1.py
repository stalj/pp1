def f(w):
    punkty=0
    samogloski=["a","e","i","o","u","y"]
    z=0
    for x in w:
        for y in samogloski:
            if x==y and z!=len(w):
                punkty+=2
            elif x==y and z==len(w):
                punkty+=3
            else:
                punkty+=1
                break
        z+=1
    return punkty

f("")
f("a")
f("water")
f("because")
f("karma")
