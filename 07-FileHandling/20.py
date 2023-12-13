with open("allproducts.txt","a") as c:
    with open("MeatAndFish.txt") as b:
        with open("FrainsAndBread.txt") as a:
            c.write(b.read() + "\n")
            c.write(a.read())