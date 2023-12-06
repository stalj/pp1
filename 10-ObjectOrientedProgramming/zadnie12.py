class TV():
    def __init__(self):
        self.is_on = False
        self.chanel_number = 1
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
            print(f'TV is {"on, chanel number: "f"{self.chanel_number}" if self.is_on else "off"}')

tv = TV()
tv.turn_on()
tv.chanel_number = 15
tv.show_status()