with open("shoppinglist.txt","w") as f:
    with open("MeatAndFish.txt", "r") as g:
        with open("GrainsAndBread.txt", "r") as h:
            for i in g:
                f.write(i)
            for i in h:
                f.write(i)