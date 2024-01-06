import random
class Thermometer():
    def __init__(self):
        self.temperature = 34.0
        self.is_on = False
    def measure(self):
        if self.is_on:
            self.temperature = round(random.uniform(34.0, 42.0), 1)
        else:
            print("Ypu can't measure temperature when the thermometer is off")
    def display(self):
        if self.is_on:
            print(f'Temperature: {self.temperature}', end="")
            if 37<=self.temperature<41:
                print(' (fever)')
            elif self.temperature >=41:
                print(' CRITICAL TEMPERATURE!')
            else:
                print("")
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False

therm = Thermometer()
therm.on()
therm.measure()
therm.display()
therm.off()