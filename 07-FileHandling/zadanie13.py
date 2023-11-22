movie_titles = ["Harry Potter", "Hunger Games", "Lord of the Rings", "Percy Jackson", "Divergent"]
file = open("movies.txt", "w")
for i in movie_titles:
    file.write(i+"\n")
file.close()
file = open("movies.txt", "r")
print(file.read())
file.close()