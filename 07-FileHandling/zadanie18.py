filenames = ['MeatAndFish.txt', 'GrainsAndBread.txt']
with open('shoppinglist18.txt ', 'w') as outfile:
    for fnames in filenames:
        with open(fnames) as infile:
            outfile.write(infile.read())