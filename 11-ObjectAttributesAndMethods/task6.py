# class definition
class Film():
    
    # class variables
    cinema = "Multikino"
    
    def __init__(self, title):
        self.title = title
    
    def __str__(self):
        return f"{self.title} ({Film.cinema})"
    
# program
film1 = Film("The Shawshank Redemption")
print(film1)
film2 = Film("Pulp Fiction")
print(film2)

# renaming the cinema (changing the value
# of a class variable) 
Film.cinema = "Cinema City "
print(film1)
print(film2)
