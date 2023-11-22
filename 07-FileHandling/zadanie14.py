file = open("shopping.txt","a")
read_product = True
counter = 0
while read_product:
    product = input("Enter product name: ")
    if product != "":
        counter += 1
        file.write(str(counter)+". "+product+"\n")
    else:
        read_product = False
file.close()
