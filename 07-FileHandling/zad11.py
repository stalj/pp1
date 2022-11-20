film_tittles=["Die Hard", "Olsen Banden", "Bad Boys", "Mamma Mia!", "The Disaster Artist"]

with open("film_tittles.txt", 'w') as f:
    for i in film_tittles:
        f.write(i)
        f.write("\n")