class Termometr():

    def __init__(self):
        self.is_on=False

    def turn_on(self):
        self.is_on=True

    def turn_off(self):
        self.is_on=False

    def check(self,temp):
        if self.is_on==True and temp<34.0 or temp>42.0:
            print("Błąd")
        elif self.is_on==True and temp>=34.0 and temp<=37.0:
            print(temp,"C, w normie")
        elif self.is_on==True and temp>37.0 and temp<=41.0:
            print(temp,"C, gorączka")
        elif self.is_on==True and temp>41.0 and temp<=42.0:
            print(temp,"C, stan krytyczny")

termometr=Termometr()
termometr.turn_on()
termometr.check(38.8)
termometr.turn_off()
termometr.check(40.0)
