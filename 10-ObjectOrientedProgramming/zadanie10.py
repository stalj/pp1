class Piece():
    def __init__(self, artist, track_title, album, year):
        self.performer = artist
        self.song = track_title
        self.album = album
        self.year = year
    def __str__(self):
        return "Performer: "+self.performer+"\n"+"Song: "+self.song+"\n"+"Album: "+self.album+"\n"+"Year:  "+self.year

piece = Piece("Queen", "Bohemian Rhapsody", "A Night at the Opera", "1975")
piece1 = Piece("Queen", "Sweet Lady", "A Night at the Opera", "1975")
print(piece)
print(piece1)