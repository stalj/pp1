class Czlowiek():

    def imie(self,imie):
        imie.self=imie

    def przedstaw_sie(self, przywitanie = "Cześć"):
        return przywitanie + ", mam na imię " + self.imie

Adam=Czlowiek()
Adam.imie="Adam"
print(Adam.przedstaw_sie("Witam"))