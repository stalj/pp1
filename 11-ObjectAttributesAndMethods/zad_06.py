class Film():
    
    # class variables
    cinema = "Multikino"
    
    def __init__(self, title):
        self.title = title
    
    def __str__(self):
        return f"{self.title} ({Film.cinema})"

x=Film("Star Wars")
print(x)