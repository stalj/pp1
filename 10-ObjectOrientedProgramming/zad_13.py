class TV():

    def __init__(self):
        self.is_on=False
        self.volume=0
    
    def turn_on(self):
        self.is_on=True
    
    def turn_off(self):
        self.is_on=False

    def volume_value(self,volume):
        self.volume=volume

    def show_status(self):
        if self.is_on==True:
            return("TV is on, volume:",self.volume)
        else:
            return("TV is off")

tv=TV()
print(tv.show_status())
tv.turn_on()
print(tv.show_status())
tv.volume_value(7)
print(tv.show_status())