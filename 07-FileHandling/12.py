# define personal data
name = "Anna May"
university = "Krakow University of Economics"
field = "Applied Informatics"

# write to a file
file = open("student.txt", "w")
file.write(name + "\n")
file.write(university + "\n")
file.write(field)

file.close()
