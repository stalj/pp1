class TV():
    
    def __init__(self):
        self.is_on=False
        self.channel=1

    def turn_on(self):
        self.is_on=True

    def turn_off(self):
        self.is_on=False

    def channel_num(self):
        x=int(input("Podaj program:"))
        self.channel=x

    def show_status(self):
        if self.is_on:
            return(f"TV is on, channel {self.channel}")
        else:
            return("TV is off")


telewizor=TV()
print(telewizor.show_status())
telewizor.turn_on()
print(telewizor.show_status())
telewizor.channel_num()
print(telewizor.show_status())