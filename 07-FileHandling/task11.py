array = ["film1", "film2", "film3", "film4", "film5"]
file = open("films_titles.txt", "w")
for i in range(5):
    file.write(f"{array[i]}\n")
file.close()