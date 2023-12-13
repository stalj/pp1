movie_titles = ["title one", "title two", "title three", "title four", "title five"]

file = open("movies.txt", "w")

index = 0
for iteration in range(len(movie_titles)):
    file.write(movie_titles[index] + "\n")
    index += 1

file.close()