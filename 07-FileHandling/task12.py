with open("shopping.txt", "a") as file:
        item= input("enter item: ")
        file.write(f"{item} \n")
