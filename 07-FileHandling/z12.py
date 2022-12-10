file = open('shopping.txt', 'a', encoding='utf-8')
file.write("\n" + input("Podaj nazwe produktu: "))
file.close()