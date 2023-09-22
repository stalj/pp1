class Plyta:
    def __init__(self, artist, title, album, year):
        self.artist=artist
        self.title=title
        self.album=album
        self.year=year
    
    def __str__(self):
        return(f"Performer:{self.artist}\nSong:{self.title}\nAlbum:{self.album}\nYear:{self.year}")

music=Plyta("Ed","Shape of you","flowers",2014)
print(music)