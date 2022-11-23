film_titles = ['Harry Potter', 'Kamień', 'Ogień', 'Dzień', 'Kamelot']
file = open('film_titles.txt', 'w',encoding='utf-8')

for i in film_titles:
    file.write(f"{i} \n ")
file.close()
