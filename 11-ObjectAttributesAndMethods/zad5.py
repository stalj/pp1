class music():
    def __init__(self, artist, album ,track_title):
        self.artist=artist
        self.track_title=track_title
        self.album=album
    def __str__(self):
        print(self.artist)
        print(self.track_title)
        print(self.album)

        
muzyk=music("Stary Grubego and his band", "Opowieści ze złomu", "Przekęty małe i duze")
muzyk.__str__()