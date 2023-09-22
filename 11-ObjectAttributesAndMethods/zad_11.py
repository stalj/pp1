class Pola_figur():

    @staticmethod
    def kolo(promień):
        pole=3.14*promień*promień
        return pole

    @staticmethod
    def trojkat(podstawa,wysokość):
        pole=podstawa*wysokość*0.5
        return pole
        
    @staticmethod
    def prostokat(bok1,bok2):
        pole=bok1*bok2
        return pole

print(Pola_figur.trojkat(6,2))
print(Pola_figur.kolo(3))
print(Pola_figur.prostokat(4,7))