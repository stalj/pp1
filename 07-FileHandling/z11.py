film_titles = ["Shrek", "Shrek 2", "Shrek the Third", "Shrek Forever After", "Shrek 5"]
file = open('filmy.txt', 'w')
for i in film_titles:
    file.write(i + "\n")
file.close()