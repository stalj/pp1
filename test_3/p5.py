class C():
    
    def __init__(self,imie,nazwisko,wiek,staz):
        self.imie=imie
        self.nazwisko=nazwisko
        self.wiek=wiek
        self.staz=staz

    def f(self):
        x=""
        x+=self.imie[:1]
        x+=self.nazwisko
        x+=str(self.wiek)
        if self.staz>=5:
            x+="+"
        return x


c=C("Anna","May",24,7)
c.f()