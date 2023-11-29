with open("MeatAndFish.txt", "r") as m:
    f = m.read()
with open("GrainsAndBread.txt", "r") as a:
    b = a.read()
with open("allproducts.txt", "w")as c:
    c.write(f)
    c.write("\n")
    c.write(b)
